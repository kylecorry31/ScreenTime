extern crate dirs;

use std::path::{Path, PathBuf};
use std::io::{self, Write, Error, ErrorKind};
use std::fs::{self, OpenOptions};

fn get_base_path() -> io::Result<PathBuf> {
    match dirs::config_dir() {
        Some(path) => Ok(path),
        None => Err(Error::new(ErrorKind::Other, "Could not get base path"))
    }
}

pub fn get_full_path<P: AsRef<Path>>(file_path: P) -> io::Result<PathBuf> {
    let mut p = get_base_path()?;
    p.push(&file_path);
    Ok(p)
}

fn create_all_dirs<P: AsRef<Path>>(path: P) -> io::Result<()> {
    match path.as_ref().parent() {
        Some(parent) => {
            fs::create_dir_all(&parent)
        },
        None => Err(Error::new(ErrorKind::Other, "Could not get parent directory"))
    }
}

#[test]
fn test_appends_and_reads_file() {
    let file = "test.txt";
    fs::remove_file(file).unwrap_or_default();
    append(file, "test\n").unwrap();
    assert_eq!("test\n", read(file).unwrap());
    append(file, "hi").unwrap();
    assert_eq!("test\nhi", read(file).unwrap());
    fs::remove_file(file).unwrap();
}

// From https://github.com/pop-os/system76-power/blob/master/src/util.rs
pub fn append<P: AsRef<Path>>(path: P, data: &str) -> io::Result<()> {
    {
        create_all_dirs(&path)?;
        let mut file = OpenOptions::new().append(true).create(true).open(&path)?;
        write!(file, "{}", data)?;
    }
    Ok(())
}

#[test]
fn test_reads_non_existant_file() {
    let file = "test4.txt";
    assert_eq!("", read(file).unwrap());
}

pub fn read<P: AsRef<Path>>(path: P) -> io::Result<String> {
    Ok(fs::read_to_string(&path).unwrap_or(format!("")))
}

#[test]
fn test_archives_file() {
    let file = "test2.txt";
    let file2 = "test3.txt";
    fs::remove_file(file).unwrap_or_default();
    fs::remove_file(file2).unwrap_or_default();
    append(file, "test\n").unwrap();
    archive(file, file2).unwrap();
    assert_eq!("test\n", read(file2).unwrap());
    assert_eq!(false, Path::new(file).exists());
    fs::remove_file(file2).unwrap();
}

pub fn archive<P: AsRef<Path>>(src_path: P, dest_path: P) -> io::Result<()> {
    fs::copy(&src_path, &dest_path)?;
    fs::remove_file(&src_path)?;
    Ok(())
}
