import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

#Defining class objects
class LineGraph:
    """
    A class to plot a line graph using Matplotlib.
    """
    
    def __init__(self, x_values, y_values, title):
        self.x_values = x_values
        self.y_values = y_values
        self.title = title
        
    def plot_line(self):
        """
        Plots the line graph using Matplotlib.
        """
        try:
            plt.plot(self.x_values, self.y_values)
            plt.title(self.title)
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.show()
        except Exception as e:
            print(f"Error: {str(e)}")

class BarChart:
    """
    A class to plot a bar chart using Matplotlib.
    """
    
    def __init__(self, x_values, y_values, x_label, y_label, title):
        self.x_values = x_values
        self.y_values = y_values
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        
    def plot_bar(self):
        """
        Plots the bar chart using Matplotlib.
        """
        try:
            plt.figure(figsize=(10, 8))
            plt.bar(self.x_values, self.y_values)
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title)
            plt.show()
        except Exception as e:
            print(f"Error: {str(e)}")

class StackedBarChart:
    """
    A class to create a stacked bar chart using Matplotlib.
    """
    def __init__(self, data, xlabel, ylabel, title):
        self.data = data
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
    
    def plot_stacked(self):
        """
        Creates a stacked bar chart using Matplotlib.
        """
        try:
            self.data.plot(kind='bar', stacked=True)
            plt.xlabel(self.xlabel)
            plt.ylabel(self.ylabel)
            plt.title(self.title)
            plt.show()
        except Exception as e:
            print(f"Error: {str(e)}")

class ScatterPlot:
    """
    A class to plot a scatter plot using Matplotlib.
    """
    
    def __init__(self, x_values, y_values, x_label, y_label, title):
        self.x_values = x_values
        self.y_values = y_values
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        
    def plot_scatter(self):
        """
        Plots the scatter plot using Matplotlib.
        """
        try:
            plt.figure(figsize=(10, 8))
            plt.scatter(self.x_values, self.y_values)
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.title(self.title)
            plt.show()
        except Exception as e:
            print(f"Error: {str(e)}")

class PieChart:
    """
    A class to create a pie chart using Matplotlib.
    """
    def __init__(self, data, labels, title):
        self.data = data
        self.labels = labels
        self.title = title
    
    def plot_pie(self):
        """
        Creates a pie chart using Matplotlib.
        """
        try:
            plt.figure(figsize=(8, 6))
            plt.pie(self.data, labels=self.labels, autopct='%1.1f%%')
            plt.title(self.title)
            plt.show()
        except Exception as e:
            print(f"Error: {str(e)}")
