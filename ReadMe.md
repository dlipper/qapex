# QApEx Utility
Simple tool to manipulate IBM QRadar data through API from command line as batch tasks or in interactive pseudo-shell.

Version: 0.0.1

## Prerequisites for script
1. Install Python 3.9 or later
2. Add additional Python modules
```
    pip install -r requirements.txt
```
3. Create the configuration file with the same name as the script and .conf extention
4. Use command line parameters or configuration file:
<pre>
    QRADAR_IP = IBM QRadar SIEM server
    TOKEN = Security token for communicating with IBM QRadar SIEM server
</pre>
5. See the inline help with -h

## Usage
### From command line
<pre>
qapex.py [-h] 

positional arguments:
  TBD             

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG_SECTION
                        Configuration section in C:\Users\DPetrashchuk\Google
                        Drive\GIT\Python Projects\qradar-export\qapi-
                        export.conf with QRADAR_IP/TOKEN parameters
  --host QRADAR_IP      IP Address of QRadar Appliance
  --token TOKEN         SEC Token
  --screen              Print on screen
  -d                    Use to turn Debug mode on
  -v                    print log to stdout
</pre>

### As Python module
<pre>
>>> import qapex
>>> qp=qapex.QApEx({'config':'TEST','screen':True, 'debug':True,'verbose':True})
>>> qp.run()
</pre>	
		
## Example of config file
<pre>
[test]
QRADAR_IP=siem.test.ua
TOKEN=XXXX-XXXX-XXXX-XXXXX
</pre>

## Release notes 
TBD
