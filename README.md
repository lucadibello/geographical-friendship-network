# Geographical-based friendship network<!-- omit in toc-->

Luca Di Bello, University of Italian Switzerland (USI), 2023

## Table of contents<!-- omit in toc-->

- [Geographical-based friendship network](#geographical-based-friendship-network)
  - [Table of contents](#table-of-contents)
  - [Project description](#project-description)
  - [Inhabitant maps](#inhabitant-maps)
    - [Purely random map](#purely-random-map)
    - [Geographical-based random map](#geographical-based-random-map)
  - [Friendship network](#friendship-network)

## Project description

Social networks are systems that map the relationships and interactions between individuals. Although social networks are typically dynamic, the focus of this project is put on a static example.

Geographical distance plays a crucial role in social network formation, with closer physical proximity typically leading to more frequent and stronger social ties.

Additionally, geographical features, such as the density of people in an area (more in cities and less in remote mountainous regions), profoundly influence the composition and scale of these networks, shaping the diversity and connectivity of communities within a given region.

## Inhabitant maps

The project features two kinds of inhabitant maps:

### Purely random map

1000 inhabitants are randomly distributed across a unit square map, $[0,1]^2$. Each individual is assigned a uniform random position $(x,y)$ in the map.

### Geographical-based random map

This map features several geographical areas $F$, such as cities, mountains, and lakes. The inhabitants are randomly distributed across the map, but the density of inhabitants is higher in cities and lower in mountains and lakes. The function $f$ maps the coordinates $(x, y)$ of an individual to the geographical area $f$ in which the individual is located.

$$
f(x,y) = \text{geographical area in which individual } (x,y) \text{ is located}
$$

In this map, individuals are no longer distributed uniformly at random across the map. Instead, the density of inhabitants depends on specific geographical features: each area has a positive factor that determines the ease of living there:

$$
\begin{equation*} \tag{1}
s_f = \text{ease of living in area } f \ \forall f \in F
\end{equation*}
$$

The probability of a random individual being located in coordinates $(x,y)$ is the following:

$$
\begin{equation} \tag{2} 
P(\text{random person settles in } (x,y)) = \frac{s_{f(x,y)}}{\sum_{(x',y') \in \text{Map}} s_{f(x',y')}}
\end{equation}
$$

## Friendship network

$$
\textcolor{red}{\textbf{FINISH THIS WHEN I HAVE SOME TIME}}
$$
