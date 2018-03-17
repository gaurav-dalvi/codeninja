# We are writing an IDE for object-oriented programmers, and working on the autocompletion feature. Because class names can be long, we want to allow users to only type the beginning of each word in a name -- so, instead of "MobileUserView", they could type "MobUsV". (Each word in the name will always start with a capital letter.)

# Given a list of class names and an input string, return all the possible autocompletions for that input string. (Autocompletions always start from the beginning, so "Data" does not match "DetailedDataView".)

# Assume the inputs are small enough that you don't need to optimize your function.

# class_names = [
#   "GraphView",
#   "DetailedDataView",
#   "DataGraphView",
#   "DataController",
#   "GraphViewController",
#   "MouseClickHandler",
#   "MathCalculationHandler",
#   "DataScienceView",
# ]

# autocomplete(class_names, "Data")            
# # Expected output: [DataController, DataGraphView, DataScienceView]

# autocomplete(class_names, "GVi")
# # Expected output: [GraphView, GraphViewController]

# autocomplete(class_names, "MCHandler")
# # Expected output: [MouseClickHandler, MathCalculationHandler]

# autocomplete(class_names, "MoCHandler")
# # Expected output: [MouseClickHandler]

# autocomplete(class_names, "MathHandler")
# # Expected output: []
