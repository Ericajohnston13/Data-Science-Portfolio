library(readr)
energy <- read_csv("C:/Users/baby_/OneDrive/Desktop/DSO104C/LESSON 1/energy.xlsx")
View(energy)

energy1 <- t(energy)

class(energy1)

energy2 <- as.data.frame(energy1)

class(energy2)

names(energy2) <- gsub("V", "Year", names(energy2))
