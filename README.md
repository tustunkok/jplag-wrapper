# JPlag Wrapper
A small program written with PyQt to provide a simple user interface to JPlag 
plagiarism software.

## Getting Started
Just get a clone of the project and run the following command.

```bash
$ python jplag_wrapper.py
```

Then choose the source directory where submission files sit and choose the 
destination directory where the output files produced by the JPlag program will
go. Select the programming language and hit start.

### Prerequisites
PyQt5 is the only dependency for the project. You can install PyQt5 with the 
following command.

```bash
$ pip install PyQt5
```

In addition to Python dependency, you need the JPlag binary. You can find it 
[here](https://github.com/jplag/jplag/releases). Download the `*.jar` file, 
rename it as `jplag.jar` and put the `jplag.jar` file to the same directory as 
the `jplag_wrapper.py` file.

## Contributing
There is no guideline or anything like that. Just send a pull request.

## Authors
* **Tolga Üstünkök** - *Initial work* - 
[tustunkok](https://github.com/tustunkok/)

## License
This project is licensed under the MIT License - see the 
[LICENSE.md](LICENSE.md) file for details.