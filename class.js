class Rectangle {
    //properties- variables
    //methods
    //belongs to the objects created for this class
    /*
        classes are a way to define blueprint for creating objects !
        declare the class
        define the blueprint of class((every object of this class))- new Rectangle , made a new object for this class !

    */
    constructor(width, height, color)
   {
    this.width=width;
    this.height=height;
    this.color=color;
   }
   area()
   {
    const area=this.width*this.height;
    return area;
   }
   paint()
   {
    console.log('Painting with color $ {this.color}');
   }

}
const rect=new Rectangle(2,3,"blue"); //instance of the rectangle class, or object of the rectangle class.
const area =rect.area();
console.log(area);
rect.paint();
console.log(paint);