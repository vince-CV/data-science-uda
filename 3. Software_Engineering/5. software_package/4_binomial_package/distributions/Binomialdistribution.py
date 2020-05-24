import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    # A binomial distribution is defined by two variables: 
    #      the probability of getting a positive outcome
    #      the number of trials
    # If you know these two values, you can calculate the mean and the standard deviation
    #      For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    # You can then calculate the mean and standard deviation with the following formula:
    #      mean = p * n
    #      standard deviation = sqrt(n * p * (1 - p))
    def __init__(self, prob=0.5, trials=20):
        """ Binomial distribution class for calculating and 
        visualizing a Binomial distribution.
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats to be extracted from the data file
            p (float) representing the probability of an event occurring
            n (int) the total number of trials
        """
        self.p = prob
        self.n = trials
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())


    def calculate_mean(self):
        """Function to calculate the mean from p and n
        Args: 
            None
        Returns: 
            float: mean of the data set
        """
        self.mean = self.p * self.n   
        return self.mean 


    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        Args: 
            None
        Returns: 
            float: standard deviation of the data set
        """
        self.stdev = (self.n * self.p * (1 - self.p))**0.5
        return self.stdev


    # The read_data_file() from the Generaldistribution class can read in a datafile. 
    # Because the Binomaildistribution class inherits from the Generaldistribution class,
    # you don't need to re-write this method. However, the method doesn't update the mean 
    # or standard deviation of a distribution. Hence you are going to write a method that
    # calculates n, p, mean and standard deviation from a data set and then updates the n, p, 
    # mean and stdev attributes.
    # Assume that the data is a list of zeros and ones like [0 1 0 1 1 0 1]. 
    #       Write code that: 
    #           updates the n attribute of the binomial distribution
    #           updates the p value of the binomial distribution by calculating the
    #               number of positive trials divided by the total trials
    #           updates the mean attribute
    #           updates the standard deviation attribute
    #       Hint: You can use the calculate_mean() and calculate_stdev() methods
    #           defined previously.
    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        Args: 
            None
        Returns: 
            float: the p value
            float: the n value
        """
        self.n = len(self.data)
        self.p = 1.0*sum(self.data)/self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p, self.n


    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        Args:
            None
        Returns:
            None
        """
        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
    
    
    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        Args:
            k (float): point for calculating the probability density function
        Returns:
            float: probability density function output
        """
        fac = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        return fac*(self.p**k)*((1 - self.p)**(self.n - k))


    
    # Use a bar chart to plot the probability density function from
    # k = 0 to k = n
    #   Hint: You'll need to use the pdf() method defined above to calculate the
    #   density function for every value of k.
    #   Be sure to label the bar chart with a title, x label and y label
    #   This method should also return the x and y values used to make the chart
    #   The x and y values should be stored in separate lists
    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution
        Args:
            None
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """
        x = []
        y = []
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')
        plt.show()

        return x, y


    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
    # Define addition for two binomial distributions. Assume that the
    # p values of the two distributions are the same. The formula for 
    # summing two binomial distributions with different p values is more complicated,
    # so you are only expected to implement the case for two distributions with equal p.
    # the try, except statement above will raise an exception if the p values are not equal
    # Hint: When adding two binomial distributions, the p value remains the same
    #   The new n value is the sum of the n values of the two distributions.
    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p
        Args:
            other (Binomial): Binomial instance
        Returns:
            Binomial: Binomial distribution
        """
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
        
        
                        
    # use the __repr__ magic method to output the characteristics of the binomial distribution object.
    # Define the representation method so that the output looks like
    #       mean 5, standard deviation 4.5, p .8, n 20
    #       with the values replaced by whatever the actual distributions values are
    #       The method should return a string in the expected format
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        Args:
            None
        Returns:
            string: characteristics of the Gaussian
        """
        return "mean {}, standard deviation {}, p {}, n {}".\
        format(self.mean, self.stdev, self.p, self.n)
