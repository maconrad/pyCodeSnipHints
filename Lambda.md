Lambdas
========

## Lambdas Basics
* Instead of explicit function
* Often Replace simple functions
* Think Anonymous function in JS
* Example problem that it solves:
    * Some functions like sort() only work with primitive types like str or int. But when it comes to a dict, they need to know based on which item to sort() etc.

```python
    # This fails with an exception (not supported)
    actors = [
        {'name': 'Batman', 'age': 30},
        {'name': 'Robin', 'age': 26},
    ]

    actors.sort()
    print(actors)
```

```python
    # valid but not pythonic

    def sorter(item):
        return item['name']

    actors = [
        {'name': 'Batman', 'age': 30},
        {'name': 'Robin', 'age': 26},
    ]

    actors.sort(key=sorter)
    print(actors)
```


```python
    # valid and clean

    actors = [
        {'name': 'Batman', 'age': 30},
        {'name': 'Robin', 'age': 26},
    ]

    # Reads as: Lambda function that accepts
    #           param called item: return item['name']
    # Sort by Name
    actors.sort(key=lambda item: item['name'])
    print(actors)

    # Sort by length of name
    actors.sort(key=lambda item: len(item['name']))
    print(actors)
```

***

## Real World Example
* Array that contains all tree elements, but cannot be sorted
* Only want to retrieve decendent if it matches a certain parent

```python
    # Example taken from Tetration App Scopes Filtering
    #  https://{{URL}}/openapi/v1/app_scopes

    def filter_array(arr, func):
        """ Filters an array based on a lambda func (=criteria) """
        return_array = []
        for item in arr:
            # Check given condition in lambda
            # Add to return array if evaluates to True
            if func(item):
                return_array.append(item)
        return return_array

    def get_children(self, parent):
        """Get immediate descendants of a certain element"""
        return filter_array(self.elements, lambda elem: elem['parent_id'] == parent['id'])

```

## Real World Example 2
* Same as before could be done with the integrated python filter function

```python
    # Example taken from Tetration App Scopes Filtering
    #  https://{{URL}}/openapi/v1/app_scopes

    def get_children(self, parent):
        """Get immediate descendants of a certain element"""
        filtered_children = list(filter(lambda elem: elem['parent_id'] == parent['id'], self.elements))
        return filtered_children
```




## Links
* See Lambda VS Code [Link](https://www.youtube.com/watch?v=KIzEJK7HhOw&list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj&index=5)
* See Tetration App Scopes [Link](https://www.cisco.com/c/en/us/td/docs/security/workload_security/tetration-analytics/sw/config/b_Tetration_OpenAPI/m_scopes.html)
