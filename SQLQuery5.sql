DATASET: https://ourworldindata.org/covid-deaths
simply querys using agregator





select location, date, total_cases, new_cases,total_deaths,population

from covidDeath
order by 1,2

--looking at total cases vs total deaths
-- shows likelihood of dyiing if you contract covid in your country
select location, date, total_cases,total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
from covidDeath
where location like '%states%'
order by 1,2


--Looking at Total Cases vs Population
-- percentage of population got covid in Brazil

select location, date, total_cases,population, (total_cases/population)*100 as infectPercentage
from covidDeath
where location like '%brazil%'
order by 1,2


-- Looking at countries with highest infection rate compared to population

select location, MAX(total_cases) as HighestInfection,population,
MAX((total_cases/population))*100 as HighestinfectPercentage
from covidDeath
Group By location, population
order by 4 desc

-- Showing countries with highest death count per Population

select location, MAX(cast(total_deaths as int)) as totalDeathCount
from covidDeath
where continent is not null
Group By location
order by 2 desc

-- Let's break things down by continent 

select continent, MAX(cast(total_deaths as int)) as totalDeathCount
from covidDeath
where continent is not null
Group By continent
order by 2 desc


-- global numbers

select SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths,
SUM(cast(new_deaths as int))/SUM(new_cases)*100 as deathpercentage
from covidDeath



-- looking at percentage people totally vaccinated


select cv.population, cv.location, cv.people_fully_vaccinated, (people_fully_vaccinated/cv.population)*100, cv.date
from covidvacinations cv
where cv.date between  '2022-07-05 00:00:00.000' and '2022-07-12 00:00:00.000' and cv.people_fully_vaccinated is not null and cv.continent is not null
order by 2


