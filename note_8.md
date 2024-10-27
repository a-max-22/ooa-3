### Dispatcher
Абстрактный класс. 
Команды: 
1. `run()`. Запустить раунд игры.
	1. предусловия: не имеется. 
	2. постусловие: запущен раунд игры. 
2. `stop().` Завершить раунд. 
	1. предусловия: раунд запущен. 
	2. постусловие: раунд завершен. 
Запросы: 
1. `is_running()`. Показывает, запущен игровой раунд или нет. 
	1. предусловие: не имеется
	2. постусловие: `RUNNING`, если запущен, `NOT_RUNNING` в противном случае. 

### GameDispatcher (Dispatcher)
Конструктор: `GameDispatcher(State)`
Команды и запросы без изменений. 

### Saveable
Абстрактный класс. Описывает элемент, который может быть сохранен в состоянии State. 
Команды:
1. `get_key()`. Запросить ключ, с которым элемент был сохранен в состояние. 
Запросы: 
1. `get_get_key_status()`. Возвращает статус операции запроса ключа.
2. `get_get_key_result()`. Возвращает последний запрошенный  ключ.

### State
Конструктор: `State()`.
Команды:
1. `save_element(Saveable elem)`. Сохранить заданный элемент в состояние.  
2. `Saveable get_element(element_id)`. Получить элемент из состояния по заданному ключу.
Запросы: 
1. `get_get_element_status()`. Возвращает статус операции запроса элемента. 
2.  `get_get_element_result()`. Возвращает последний запрошенный элемент.
3. `get_save_element_status()`. Статус операции сохранения элемента 
4. `get_save_element_key()`. Возвращает ключ для последнего сохраненного элемента. 


### Event
Конструктор: Абстрактный класс. 
Команды:
1. `apply_event(State)`. Событие применено к заданному состоянию.
   Предусловие: событие не применялось ранее
   Постусловие: Состояние изменено с помощью события 
Запросы: 
1. `get_apply_event_status()` - ошибка, если заданное событие применялось ранее. 

### Element
Конструктор: `Element(Properties)`. 
Команды:
1. `get_property(property_name)`. Получить свойство элемента. 
   Предусловие:  свойство с заданным  именем присутствует у элемента.
   Постусловие: возвращено свойство с заданным именем. 
Запросы: 
1. `get_property_status()`

### Cell
Конструктор: `Cell()` 
Команды:
1. `get_element()`. Получить размещенный  в ячейке элемент. 
   Предусловие: ячейка непуста
   Постусловие: возвращен текущий элемент, находящий в ячейке
Запросы: 
1. `is_empty()`
2. `get_element_status()`
3. `get_element_result()`

### Field
Конструктор: `Field(height, width)` 
Команды: 
1. `get_cell(x,y)`. Получить текущую клетку
   Предусловие: x,y находится в пределах поля
   Постусловие: текущий клетка установлена в запрашиваемую по заданным координатам. 
Запросы  - для получения статуса выполнения команд:
1. `get_get_cell_status()`
2. `get_get_cell_result()`

### Renderer
Абстрактный класс
Команды: 
1. `update_layout(State)`. Вычислить новое изображение для всех отображаемых элементов
2. `draw()`. Вывести новые изображения. 
3. `clear()`. Очистить поле, в котором отображаются элементы. 
Запросы  - для получения статуса выполнения команд: 
1. `update_layout(State)`
2. `get_draw_status()`
3. `get_clear_status()`

### FigureTree
Конструктор: `FigureGraph()` - инициализирует дерево с  корневым элементом (дерево не может быть пустым).   
Команды: 
1. `add_child(Val)`. Добавить дочерний элемент к текущему узлу. 
   Предусловие: не имеется
   Постусловие: добавлена дочерняя вершина   
1. `switch_to_child()`
2. `switch_to_sibling()`
   Предусловие: существует как минимум один соседний узел
   Постусловие: курсор смещен к соседней вершине
3. `switch_to_parent()`
   Предусловие: существует как минимум один родительский узел
   Постусловие: курсор смещен к родительской вершине
4. `get_current_node_val()`. 
   Предусловия: текущий узел установлен не в корневой .
   Постусловие: возвращает значение текущего узла. 
5. `switch_to_root()`.   
	Постусловие: Курсор смещен к корневой вершине. 

Запросы: 
1. `get_add_child_status(State)` - статус команды добавления дочернего узла. 
2. `get_switch_to_child_status()` - статус команды получения дочернего  узла. 
3. `get_switch_to_parent_status()` -  статус команды получения родительского  узла. 
4. `get_get_current_node_val_status()` - получить значение текущего  узла в дереве (за исключением корневого). 
5. `count_nodes()` - получить количество узлов в дереве (за исключением root).