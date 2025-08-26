# regex-automata
A Python regex script that automatically goes through a range and uses regex on it.

It accepts an endpoint URL, a value for a form-data (listed below as "password"), a range of numbers (eg. 100-200), and a regex string. It will print the output to output.txt

Can be modified to do other things.

# Usage
Adding `python` is important because the script won't work without it.
`python automata.py "http://example.com/sample_endpoint.php" password 100 200 \".\/file.*\"`
