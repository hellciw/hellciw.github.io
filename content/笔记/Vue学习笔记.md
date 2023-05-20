Title: Vue学习笔记
Date: 2023-5-10 10:00:00
Category: Vue
tags: hellciw

# Vue学习笔记

## 一、二维数组尝试

```js
var vm = new Vue({
    el: "#app",
    data: {
    huilv:[
    [6.8540, 132.9787, 1298.7013, 1.3278],
    [6.8540, 132.9787, 1298.7013, 1.3278]
        ],}
```

## 二、watch监听实现

```js
watch: {
    First: function(newValue){
    this.second = newValue * this.huilv[Number(this.firstbutton - 1)][Number(this.secondbutton -1)];
                    },
    Second: function(newValue){
    
    this.first = newValue / this.huilv[Number(this.firstbutton - 1)][Number(this.secondbutton -1)];
    
                    }
}
```

## 三、数组的更新检测

### #变更方法

Vue 将被侦听的数组的变更方法进行了包裹，所以它们也将会触发视图更新。这些被包裹过的方法包括：

> - `push()`
> - `pop()`
> - `shift()`
> - `unshift()`
> - `splice()`
> - `sort()`
> - `reverse()`

你可以打开控制台，然后对前面例子的 `items` 数组尝试调用变更方法。比如 `example1.items.push({ message: 'Baz' })`。
