fn main() {
    fn_1();
    fn_2();
    fn_3();
}
fn fn_1() {
    let maybe_value: Option<i32> = Some(42);

    match maybe_value {
        Some(value) => println!("The value is: {}", value),
        None => println!("No value found"),
    }
}

fn fn_2() {
    let my_list = vec![1, 2, 3, 4, 5];

    match my_list.get(2) {
        Some(value) => println!("The value is: {}", value),
        None => println!("No value found"),
    }
}

enum FileReadError {
    NotFound,
    PermissionDenied,
    FileAlreadyOpen,
}

fn fn_3() {
    let result_value: Result<i32, FileReadError> = Ok(100);

    match result_value {
        Ok(value) => println!("The value is: {}", value),
        Err(FileReadError::NotFound) => println!("File not found"),
        Err(FileReadError::PermissionDenied) => println!("Permission denied"),
        Err(FileReadError::FileAlreadyOpen) => println!("File is already open"),
    }
}
