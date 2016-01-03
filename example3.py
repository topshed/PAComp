# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

from adxl345p3 import ADXL345
  
adxl345 = ADXL345()
    
axes = adxl345.getAxes(True)
print ("ADXL345 on address 0x{:x}:".format(adxl345.address))
print ("   x = {:0.3f}G".format( axes['x'] ))
print ("   y = {:0.3f}G".format( axes['y'] ))
print ("   z = {:0.3f}G".format( axes['z'] ))
