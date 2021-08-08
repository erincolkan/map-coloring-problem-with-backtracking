import plotly.express as px
from random import *

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]

#Necessary classes to represent an appropriate map.
class Country:  
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = None

    #Paint the country in given color.
    def paintCountry(self, color):
        self.color = color

    #Remove the color of a country. For better semantics. 
    def removeColor(self):
        self.color = None

    #Add a neighboring country to this country object.
    def addNeighbors(self, *neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)   
        
class Map:
    def __init__(self):
        #List that holds the countries.
        self.countries = []

    #This function checks if it is safe to paint a country to a given color by checking country's neighbors.    
    def isSafe(self, c1, color):
        for neighbor in c1.neighbors:
            if neighbor.color == color:
                return False
        
        return True
    
    #Add a country to the map. For better semantics. Not something fundamental.    
    def addCountry(self, country):
            self.countries.append(country)

    #Check if c2 is a neighbor of c1.
    def isNeighbor(self, c1, c2):
        if c2 in c1.neighbors:
            return True
        
        return False 

    #This function is required in order to be able to print the map since plot_cloropleth function requires a dict inside.
    #This function returns a dictionary of each country with their corresponding colors.
    def mapAsDict(self):
        countriesDict = {}
        for country in self.countries:
            countriesDict[country.name] = country.color
        
        return countriesDict
    
    #Buradaki countrylerin her biri yeni bir instance o yuzden program calismiyor. Tekrardan bak.
    def initializeMap(self):
        southAmerica = Map()

        #Define countries.
        argentina = Country("Argentina")
        bolivia = Country("Bolivia") 
        brazil = Country("Brazil")
        chile = Country("Chile")
        colombia = Country("Colombia")
        ecuador = Country("Ecuador")
        falklandislands = Country("Falkland Islands")
        guyana = Country("Guyana")
        paraguay = Country("Paraguay")
        peru = Country("Peru")
        suriname = Country("Suriname")
        uruguay = Country("Uruguay")
        venezuela = Country("Venezuela")

        #Add neighbors of the countries.
        argentina.addNeighbors(bolivia, chile, paraguay, uruguay, brazil)
        bolivia.addNeighbors(argentina, brazil, chile, paraguay, peru)
        brazil.addNeighbors(argentina, bolivia, colombia, guyana, paraguay, peru, suriname,uruguay,venezuela)
        chile.addNeighbors(argentina, bolivia,peru)
        colombia.addNeighbors(brazil, ecuador,peru,venezuela)
        ecuador.addNeighbors(colombia,peru)
        guyana.addNeighbors(brazil,suriname,venezuela)
        paraguay.addNeighbors(argentina,bolivia,brazil)
        peru.addNeighbors(bolivia,brazil,chile,colombia,ecuador)
        suriname.addNeighbors(brazil,guyana)
        uruguay.addNeighbors(argentina,brazil)
        venezuela.addNeighbors(brazil,colombia,guyana)

        #Add each country to the map with their neighbors.
        southAmerica.addCountry(argentina)
        southAmerica.addCountry(bolivia)
        southAmerica.addCountry(brazil)
        southAmerica.addCountry(chile)
        southAmerica.addCountry(colombia)
        southAmerica.addCountry(ecuador)
        southAmerica.addCountry(falklandislands)
        southAmerica.addCountry(guyana)
        southAmerica.addCountry(paraguay)
        southAmerica.addCountry(peru)
        southAmerica.addCountry(suriname)
        southAmerica.addCountry(uruguay)
        southAmerica.addCountry(venezuela)

        #Return the map.
        return southAmerica

    #This method will only print the result with respect to result of __BacktrackSearchUtil__ function.
    def BacktrackSearch(self):
        if self.__BacktrackSearchUtil__(0):
            print("Solution exists.")
        else: 
            print("Solution doesn't exist.")

    #The real method that does the job.
    def __BacktrackSearchUtil__(self, countryIndex):
        if countryIndex == len(self.countries):
            return True
        
        #Shuffle the array to achieve different coloring each time.
        shuffle(colors)

        for color in colors:
            if self.isSafe(self.countries[countryIndex], color):
                self.countries[countryIndex].paintCountry(color)

                if self.__BacktrackSearchUtil__(countryIndex + 1):
                    return True
                
                self.countries[countryIndex].removeColor()

        return False    

# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                         locations=countries,
                         color=countries,
                         color_discrete_sequence=[colormap[c] for c in countries],
                         scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    #Initialize the map and perform the backtrack search.
    southAmerica = Map().initializeMap()
    southAmerica.BacktrackSearch()

    #Convert the result into a dictionary. 
    dictionary = southAmerica.mapAsDict()

    #Print the dictionary to the terminal. For testing purposes.
    #print(dictionary)

    #Color and show the map.    
    plot_choropleth(colormap=dictionary)

