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

fn get_full_path<P: AsRef<Path>>(file_path: P) -> io::Result<PathBuf> {
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

// From https://github.com/pop-os/system76-power/blob/master/src/util.rs
pub fn append<P: AsRef<Path>, S: AsRef<[u8]>>(path: P, data: S) -> io::Result<()> {
    {
        let p = get_full_path(&path)?;
        create_all_dirs(&p)?;
        let mut file = OpenOptions::new().append(true).create(true).open(&p)?;
        file.write_all(data.as_ref())?
    }

    Ok(())
}

pub fn read<P: AsRef<Path>>(path: P) -> io::Result<String> {
    let p = get_full_path(&path)?;
    create_all_dirs(&p)?;
    OpenOptions::new().append(true).create(true).open(&p)?;
    Ok(fs::read_to_string(&p)?)
}

pub fn archive<P: AsRef<Path>>(src_path: P, dest_path: P) -> io::Result<()> {
    let src_p = get_full_path(&src_path)?;
    let dest_p = get_full_path(&dest_path)?;
    fs::copy(&src_p, &dest_p)?;
    fs::remove_file(&src_p)?;
    Ok(())
}
