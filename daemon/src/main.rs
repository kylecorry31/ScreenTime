extern crate chrono;

use chrono::prelude::*;
use chrono::TimeZone;

mod files;

use std::io;
use std::{thread, time};

const THIS_WEEK_FILENAME: &'static str = "screen-time/week.txt";
const LAST_WEEK_FILENAME: &'static str = "screen-time/last-week.txt";

fn main() {
    start_daemon().unwrap();
}

fn start_daemon() -> io::Result<()> {
    let delay = 1000;
    println!("Logging screen time in the background.");

    sleep(delay);

    let mut last_updated = get_time()?;

    // TODO: get last time from file
    let file_contents = files::read(THIS_WEEK_FILENAME)?;
    // Maybe trim? or remove last \n
    let lines = file_contents.split("\n").collect::<Vec<&str>>();

    if lines.len() > 0 {
        let mut last = lines[lines.len() - 1];
        if last.is_empty() && lines.len() > 1 {
            last = lines[lines.len() - 2];
        }

        if !last.is_empty() {
            last_updated = last.parse::<i64>().unwrap();
        }
    }

    loop {
        let current_time = get_time()?;

        if should_archive(current_time, last_updated){
            println!("Archiving week file.");
            files::archive(THIS_WEEK_FILENAME, LAST_WEEK_FILENAME)?;
        }

        files::append(THIS_WEEK_FILENAME, format!("{}\n", current_time))?;

        last_updated = current_time;
        sleep(delay);
    }
}


pub fn get_time() -> io::Result<i64> {
    let dt = Local::now();
    Ok(dt.timestamp())
}


pub fn sleep(millis: u64) {
    let timeout = time::Duration::from_millis(millis);
    thread::sleep(timeout);
}


pub fn should_archive(current_time: i64, last_updated: i64) -> bool {
    let dt1 = Local.timestamp_millis(current_time);
    let dt2 = Local.timestamp_millis(last_updated);

    // less than 7 days apart and current_time is on a day of the week after last_updated
    !((dt1.num_days_from_ce() - dt2.num_days_from_ce() < 7) && (dt1.weekday().number_from_sunday() >= dt2.weekday().num_days_from_sunday()))
}
