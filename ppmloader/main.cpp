#include <iostream>
#include<stdio.h>
#include "ppmloader.h"
#include<vector>
#include <string>
#include <sstream>
// centro esfera, x = 244, y = 144
using namespace std;
using std::vector;
typedef unsigned char uchar;

// Ejemplo de como  acceder a los pixeles de una imagen RGB
unsigned int get_pixel_average(uchar* data, int i, int j, int height, int width){
  if(i > height)
    throw std::runtime_error("El direccionamiento vertical no puede ser mayor a la altura.");
  if(j > width)
    throw std::runtime_error("El direccionamiento horizontal no puede ser mayor al ancho.");
  unsigned int red = (unsigned int)(data[i*width*3 + j*3 + 0]);
  unsigned int green = (unsigned int)(data[i*width*3 + j*3 + 1]);
  unsigned int blue = (unsigned int)(data[i*width*3 + j*3 + 2]);
  return (unsigned int)((red+green+blue) / 3);
}

void read_image(std::string filename, uchar** data, int* width, int* height){
  *data = NULL;
  *width = 0;
  *height = 0;
  PPM_LOADER_PIXEL_TYPE pt = PPM_LOADER_PIXEL_TYPE_INVALID;

  bool ret = LoadPPMFile(data, width, height, &pt, filename.c_str());
  if (!ret || width == 0|| height == 0|| pt!=PPM_LOADER_PIXEL_TYPE_RGB_8B){
    throw std::runtime_error("Fallo al leer la imagen.");
  }
}

void test_image(){
  uchar* data = NULL;
  int width = 0, height = 0;
  std::string filename = "prueba.ppm";
  read_image(filename, &data, &width, &height); // Ejemplo de llamada

  for (int h = 0; h < height; ++h){
    for (int w = 0; w < width; ++w){
      cout << get_pixel_average(data, h, w, height, width) << " "; // Ejemplo de lectura de un pixel
    }
    cout << endl;
  }
  delete [] data;
}

vector<unsigned int> get_max_pixel(std::string filename){
    uchar* data = NULL;
    int width = 0, height = 0;
    read_image(filename, &data, &width, &height);
    vector<unsigned int> max (2,0);
    unsigned int max_value = get_pixel_average(data, max.at(0), max.at(1), height, width);
    std::cout << width << std::endl;
    std::cout << height << std::endl;
    int count = 0;
    for (int h = 0; h < height; ++h){
        for(int w = 0; w < width; ++w){
            unsigned int temporal_value = get_pixel_average(data, h, w , height, width);
            if (temporal_value > 0){
                count++;
            }
            if (max_value <= temporal_value){
                max[0] = w;
                max[1] = h;
                max_value = temporal_value;
                std::cout << "New max value: " << std::endl;
                std::cout << max_value << std::endl;
                std::stringstream ss;
                ss << "Position of temporal maximum brightness: x = " << max.at(0) << " y = " << max.at(1) << std::endl;
                std::cout << ss.str();
            }
        }
    }
//    std::cout << count << std::endl;

    return max;

};

unsigned int get_radio(std::string filename){
    uchar* data = NULL;
    int width = 0, height = 0;
    read_image(filename, &data, &width, &height);
    vector<unsigned int> highest (2, height - 1);
    vector<unsigned int> lowest (2,0);
    vector<unsigned int> leftest (2, width - 1);
    vector<unsigned int> rightest (2, 0);
    std::stringstream ss;
    for (int h = 0; h < height; ++h){
        for(int w = 0; w < width; ++w){
            unsigned int temporal_value = get_pixel_average(data, h, w , height, width);
            if(temporal_value > 0){
                if(h > lowest.at(1)){
                    lowest[1] = h;
                    lowest[0] = w;
                }
                if(h < highest.at(1)){
                    highest[1] = h;
                    highest[0] = w;
                }
                if(w < leftest.at(0)){
                    leftest[1] = h;
                    leftest[0] = w;
                }
                if(w > rightest.at(0)){
                    rightest[1] = h;
                    rightest[0] = w;
                }
            }
        }
    }
    ss << "Lowest: x = " << lowest.at(0) << " y = " << lowest.at(1) << std::endl;
    ss << "Highest: x = " << highest.at(0) << " y = " << highest.at(1) << std::endl;
    ss << "Rightest: x = " << leftest.at(0) << " y = " << rightest.at(1) << std::endl;
    ss << "Leftest: x = " << rightest.at(0) << " y = " << leftest.at(1) << std::endl;
    std::cout << ss.str();
    return (unsigned int)((lowest.at(1) - highest.at(1)) / 2);
}

void test_load(){

  uchar* data = NULL;
  int width = 0, height = 0;
  PPM_LOADER_PIXEL_TYPE pt = PPM_LOADER_PIXEL_TYPE_INVALID;
//  std::string filename = "buda.0.ppm";
  std::string filename = "prueba.ppm";

  bool ret = LoadPPMFile(&data, &width, &height, &pt, filename.c_str());
  if (!ret || width == 0|| height == 0|| pt!=PPM_LOADER_PIXEL_TYPE_RGB_8B)
  {
    throw std::runtime_error("test_load failed");
  }

  delete [] data;
}

void test_save(){

  char comments[100];
  sprintf(comments, "%s", "Hello world");

  int width = 3, height =1;
  uchar* data = new uchar[width*height*3];
  data[0] = data[1] = data[2] = 100; // RGB
  data[3] = data[4] = data[5] = 150; // RGB
  data[6] = data[7] = data[8] = 245; // RGB
  std::string filename = "prueba.ppm";

  bool ret = SavePPMFile(filename.c_str(),data,width,height,PPM_LOADER_PIXEL_TYPE_RGB_8B, comments);
  if (!ret)
  {
    std::cout << "ERROR: couldn't save Image to ppm file" << std::endl;
  }
}

int main() {
  test_load();
  test_save();
  test_image();
    std::cout << "Choose a image from the folder: ...  ";
    std::string filename = "";
    std::cin >> filename;
  vector<unsigned int> max = get_max_pixel(filename);
    std::stringstream ss;
    ss << "Position of maximum brightness: x = " << max.at(0) << " y = " << max.at(1) << std::endl;
    std::cout << ss.str();
    unsigned int radio = get_radio("mate.mask.ppm");
    std::cout << radio << std::endl;
    std::cout << filename << std::endl;
  return 0;
}
