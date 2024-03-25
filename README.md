## <img src="assets/python_logo.png" alt="drawing" width="70"/> Файловый менеджер на Python

__Выполнение проекта:__ _Удовенко Артём Б05-323_
### Общее описание
>Проект направлен на создание полноценного файлового менеджера - интерфейса, который предоставляет пользователю возможность быстро и удобно манипулировать файлами и директориями.
>
Первая версия приложения будет работать через консоль Python путем запуска соответствующего скрипта. В дальнейшем планируется создать GUI при помощи библиотеки [tkinter](https://docs.python.org/3/library/tkinter.html). Проект поддерживается на любой операционной системе, необходимо наличие версии Python не ниже [3.0.0](https://www.python.org/downloads/release/python-300/). Необходима установка библиотеки [keyboard](https://thepythoncode.com/article/control-keyboard-python).
******
### Функционал
Менеджер будет поддерживать следующие операции:
- перемещение между директориями
```python
cd some_directory #go to some_directory
```
- копирование, вырезание, вставка файлов и директорий, работа с буфером
```python
copy test.txt #place file in the buffer
paste #insert file in working directory
buf-show #print absolute path to file in buffer
```
- удаление и перемещение файлов и директорий
```python
delete test.txt #remove file from wd
```
- переименование и вывод свойств файла
```python
rename test1.txt test2.txt #set name to test2.txt
```
- запуск любых файлов (в том числе исполняемых)
```python
exec test.txt #run the file
```
- графическая древовидная интерпретация директории
```python
graph #show directory's structure
```
- undo и redo
```python
undo #return the previous state
```
- создание сценариев работы
```python
scen move > (copy $1$) (cd $2$) (paste) #perform consistently
```
- настройка hot keys
```python
hot-key <scenario_name> #assign some hot key
```
Больше команд и примеров с подробным гайдом будет изложено в документации.
******
### Реализация и архитектура
Архитектура проекта отражена на UML-диаграмме. Во время реализации классы и методы будут доработаны.

![UML](assets/UML-diagram_classes.bmp)


