'use strict';
// 1st
// Call the ride method of the volvo, with 42 as a parameter

var volvo = {
  type: "Volvo",
  fuel: 23,
  consumption: 0.06,
  kms: 43000,
  ride: function (km) {
    this.kms += km;
    this.fuel -= km * this.consumption; 
  }
};

volvo.ride(42);



// 2nd
// Call the refuel function on the ferrari object using the bind method, with
// 52 as a parameter

var ferrari = {
  type: "Ferrari",
  fuel: 0,
  consumption: 0.12,
  kms: 9000,
  ride: function (km) {
    this.kms += km;
    this.fuel -= km * this.consumption; 
  }
};

function refuel(liters) {
  this.fuel += liters
}

// refuel(52).apply(ferrari)
refuel.bind(ferrari)(52);





// 3rd
// Create a tesla object that has 3 properties
//  - type: string
//  - battery: number
//  - kms: number
//  - consunption: number
// And a method called ride, that takes a parameter celled km,
// and increments kms with it, then drains the battery based on the consumpltion 


var tesla = {
    type: "Tesla",
    battery: 75, // kWh/100 km
    kms: 390, // Range
    consumption: 20,
    ride: function (km) {
        this.kms -= km;
        this.battery -= km / 100 * this.consumption; 
    }
}


tesla.ride(36);
console.log(tesla.kms + " km range until charging.");
console.log(tesla.battery + " kWh energy left in buttery.");