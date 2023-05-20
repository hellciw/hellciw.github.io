title: CSS样式笔记
Date: 2023-5-17 10:00:00
Category: Css
tags: hellciw

# CSS样式笔记

## 1、关于对div样式横置

```
display：flex   or   float：left
```



## 2、center的作用域text-align:center

```
`text-align` CSS 属性定义行内内容（例如文字）如何相对它的块父元素对齐。`text-align` 并不控制块元素自己的对齐，只控制它的行内内容的对齐。
```



### 1)常见的行内元素

```
 <span>、<a>、 <img>、 <input>、<textarea>、<select>、<label>
 还有包括一些文本元素如：<br>  、<b>、 <strong>、<sup> 、<sub>、 <i> 、<em> 、<del> 、 <u>等。
 不能只回答<img>和<a>吧！
```



### 2)常见的块级元素

```
<div> <table> <form> <p> <ul>  <h1>......<h6> <hr>   <pre> <address> <center> <marquee>  <blockquote>  等。
```



### 3)区别

#### -块级元素

1. 总是从新的一行开始，即各个块级元素独占一行，默认垂直向下排列；
2. 高度、宽度、margin及padding都是可控的，设置有效，有边距效果；
3. 宽度没有设置时，默认为100%；
4. 块级元素中可以包含块级元素和行内元素。

#### -行内元素

1. 其他元素都在一行，即行内元素和其他行内元素都会在一条水平线上排列；
2. 高度、宽度是不可控的，设置无效，由内容决定。
3. 根据标签语义化的理念，行内元素最好只包含行内元素，不包含块级元素。