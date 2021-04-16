# Giraphics
![Banner](https://github.com/tghira16/GiraFix/blob/master/res/banner.svg?raw=true=250x)

Giraphics is graphing and animation library designed to fast and simple to use. The library is inspired by [3b1b]'s [manim] library, but built independently.
## Installation
The core package can be installed with `pip`.

```
pip install giraphics
```

Basic graphing and plotting can be done without any other software, however, the following packages are required for full functionality.
* [librsvg]: Used to convert SVG to other image formats
* [ffmpeg]: Used to convert images into a video 
* [tex2svg]: Used to render LaTex

Individual packages can be installed for specific functionality, but installation of all packages is reccomended.
## Examples
Here are some example with what can be made with the `Giraphics`

### Vector fields
![s]

### Animation 
Here is an example of the Sine series, every second we add a new term the Taylor expansion of Sine.
![Sine Series](https://github.com/tghira16/Giraphics/blob/2ee931665e40ac08abc7c3d5c1e786850b206071/Examples/TaylorSeriesSine.gif)


## Tutorial 
You can find the tutorial [here]

## Contribution
You can make pull requests.

## Issues 

* The cleanup option does not work in `Animation.develop()`
## License
Mit License

[ffmpeg]: <https://ffmpeg.org/>
[3b1b]: <https://github.com/3b1b>
[manim]: <https://github.com/3b1b/manim>
[librsvg]: <https://github.com/GNOME/librsvg>
[tex2svg]: <https://github.com/mathjax/mathjax-node-cli/blob/master/bin/tex2svg>
[plot]: <https://github.com/tghira16/GiraFix/blob/master/Examples/graph_example.py>
[complexplot]: <https://github.com/tghira16/GiraFix/blob/master/Examples/Complex_Function_Example.py>
[vectorfield]: <https://github.com/tghira16/GiraFix/blob/master/Examples/Vector_field_example.py>
[here]: <https://github.com/tghira16/Giraphics/blob/master/tutorial.md>
