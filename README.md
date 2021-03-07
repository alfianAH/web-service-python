# Web Service with Python

Using requests package in python to post feedback to website.

## Get Started
1. Clone this repository
2. Before you run the script, check your OS in the script. If you use Linux, make sure you uncomment the linux line in [run.py](run.py). Default is `For Windows`.
3. The `website` variable is the place to post the dictionary. Make sure you change `website` variable before running it.

## Example
This is the example dictionary for [001.txt](data/feedback/001.txt)

```
{
    'title': 'Great Customer Service', 
    'name': 'John', 
    'date': '2017-12-21', 
    'feedback': 'The customer service here is very good. They helped me find a 2017 Camry with good condition in reasonable price. Campared to other dealers, they provided the lowest price. Definttely recommend!'
}
```

## Preview
If the `POST` request is successful, the result will become like this

![Result](markdown/result.png)