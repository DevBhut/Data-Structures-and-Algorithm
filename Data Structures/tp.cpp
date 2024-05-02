#include <iostream>
using namespace std; 
// creating Animal class
class Animal{
    bool gives_birth;    
    bool lay_egg;    
    bool live_in_ground;    
    bool live_in_water;    
    bool have_wings;};
    
    int main(){    
        // creating an object of animal class    
        Animal mammal;        
        //assign values to instance variables    
        mammal.gives_birth = true;    
        mammal.lay_egg = false;    
        mammal.live_in_ground = true;    
        mammal.live_in_water = false;    
        mammal.have_wings = false;    
        
        Animal amphibian;    
        amphibian.gives_birth = false;    
        amphibian.lay_egg = true;    
        amphibian.live_in_ground = true;    
        amphibian.live_in_water = true;    
        amphibian.have_wings = false;    
        
        Animal bird;    
        bird.gives_birth = false;    
        bird.lay_egg = true;    
        bird.live_in_ground = true;    
        bird.live_in_water = false;    
        bird.have_wings = true;

        return 0;
        
    }

