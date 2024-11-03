//quadratic equation calculator 
var a: Double = 3.0
var b: Double = -11.0
var c: Double = -4.0
var root1 = (b*b) - (4*a*c)
var root2 = (-b - (b*b - 4*a*c).squareRoot()) / (2*a)
root1=root1.squareRoot()
root1 = -b + root1
root1 = root1 / (2*a)
print ("root 1 is \(root1)")
print ("root 2 is \(root2)")