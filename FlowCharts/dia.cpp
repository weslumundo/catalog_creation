#include <iostream>
#include <string>
int global = 1;


//There is a lot of useless code in this file, i dont like to delete things. Until I clean this up I would recommend renaming "main" something else and making a new main function with your own diagram inside, also this code probably only works on the eecs cycle servers

std::string makeNode(int id, std::string title, std::string shape = "record"){
	return "node" + std::to_string(id) + " [shape="+shape+" label=\""+title+"\"]\n";
}

std::string makeConn(int first, int second){
return "node" + std::to_string(first) + " -> node" + std::to_string(second) + " [label=\"\"]\n";
}

int mainM(){
	std::string myNodes;
	std::string myConn;
	std::string myConn2;
	std::string myNodes2;
	myNodes += makeNode(10000000,"User Input","triangle");
	
	myNodes += makeNode(1,"All Weight Images");
	myNodes += makeNode(2,"All Images");
	myNodes += makeNode(3,"All Segmentation Images");
	myNodes += makeNode(4,"All Mask Images");
	myNodes += makeNode(5, "All C values");
	myNodes += makeNode(6, "default_dualimage.sex","triangle");
	myNodes += makeNode(7,"making_a_catalog.ipynb","octagon");
	myNodes += makeNode(8,"Catalog");
	
	myConn2 += makeConn(1,7);
	myConn2 += makeConn(2,7);
	myConn2 += makeConn(3,7);
	myConn2 += makeConn(4,7);
	myConn2 += makeConn(5,7);
	myConn2 += makeConn(6,7);
	myConn += makeConn(7,8);
	

	
	
	std::cout<<myNodes;
	std::cout<<"subgraph cluster_R{\n";
	std::cout<<myNodes2;
	std::cout<<myConn2;
	std::cout<<"label = \"Catalog Creation\"";
	std::cout<<"}\n";
	std::cout<<myConn;
	return 0;
}

int mainC(){
	std::string myNodes;
	std::string myConn;
	std::string myConn2;
	std::string myNodes2;
	myNodes += makeNode(10000000,"User Input","triangle");
	
	myNodes += makeNode(1,"Reprojected Image");
	myNodes += makeNode(2,"Target Image");
	myNodes += makeNode(3, "Source FWHM","triangle");
	myNodes += makeNode(4, "Target FWHM","triangle");
	myNodes2 += makeNode(5,"Convolutin_py3_v2.ipynb","octagon");
	myNodes += makeNode(6,"Convoluted Image");
	
	myConn2 += makeConn(1,5);
	myConn2 += makeConn(2,5);
	myConn2 += makeConn(3,5);
	myConn2 += makeConn(4,5);
	myConn += makeConn(5,6);
	

	
	
	std::cout<<myNodes;
	std::cout<<"subgraph cluster_R{\n";
	std::cout<<myNodes2;
	std::cout<<myConn2;
	std::cout<<"label = \"Convolution Class\"";
	std::cout<<"}\n";
	std::cout<<myConn;
	return 0;
}
int mainR(){
	std::string myNodes;
	std::string myConn;
	std::string myConn2;
	std::string myNodes2;
	
	myNodes += makeNode(1,"Source Image");
	myNodes += makeNode(2,"Source Weight Image");
	myNodes += makeNode(3,"Target Image");
	myNodes += makeNode(4,"Target Weight Image");
	myNodes2 += makeNode(5,"reproj_kmj.py","octagon");
	myNodes += makeNode(6,"Reprojected Image");
	myNodes += makeNode(7,"Reprojected Weight Image");
	myConn2 += makeConn(1,5);
	myConn2 += makeConn(2,5);
	myConn2 += makeConn(3,5);
	myConn2 += makeConn(4,5);
	myConn += makeConn(5,6);
	myConn += makeConn(5,7);
	
	
	std::cout<<myNodes;
	std::cout<<"subgraph cluster_R{\n";
	std::cout<<myNodes2;
	std::cout<<myConn2;
	std::cout<<"label = \"Reprojection Class\"";
	std::cout<<"}\n";
	std::cout<<myConn;
	return 0;
}

int mainE(){
	
	std::string myNodes;
	std::string myConn;
	std::string myConn2;
	std::string myConn3;
	myNodes += makeNode(10000000,"User Input","triangle");
	
	myNodes += makeNode(3,"Source Extractor","octagon");
	myNodes += makeNode(4,"maskitextra.py","octagon");
	myNodes += makeNode(200,"Pixel scale","triangle");
	myNodes += makeNode(201,"default_objsub_norm.sex","triangle");
	myConn  += makeConn(101,4);
	myConn  += makeConn(102,4);
	myNodes += makeNode(5, "Normalized Image");
	myConn2 += makeConn(4,5);
	myConn2 += makeConn(5,3);
	myConn2 += makeConn(200,11);
	myConn2 += makeConn(201,3);
	
	myNodes += makeNode(7,"Object Subtracted Image");
	myConn += makeConn(3,6);
	myConn2 += makeConn(3,7);
	myConn += makeConn(4,9);
	myNodes += makeNode(8, "quickmask.py","octagon");
	myNodes += makeNode(11, "runEAA.py","octagon");
	myNodes += makeNode(9,"Mask Image");
	
	myNodes += makeNode(10,"Masked Object Subtracted Image");
	myConn2 += makeConn(9,8);
	myConn2 += makeConn(7,8);
	myConn3 += makeConn(8,10);
	myConn3 += makeConn(10,11);
	myConn2 += makeConn(11,12);
	myConn2 += makeConn(11,13);
	myConn2 += makeConn(12,14);
	myConn2 += makeConn(13,14);
	myConn += makeConn(9,90);
	
	myNodes += makeNode(14, "WorkingDepth", "octagon");
	myConn += makeConn(14,15);
	myNodes += makeNode(15,"C values");
	
	
	
	
	std::cout<<myNodes;
	
	std::cout<<"subgraph cluster_A{\n";
	std::cout<<"subgraph cluster_R{\n";
	std::cout<<myConn3;
	std::cout<<"label = \"Empty Apperature Analysis\"";
	std::cout<<"}\n";
	std::cout<<myConn2;
	std::cout<<"label = \"Error Calculation\"";
	
	std::cout<<"}\n";
	std::cout<<myConn;
	
	return 0;
}

int mainG(){
	std::string myNodes;
	std::string myConn;
	myNodes += makeNode(10000000,"User Input","triangle");
	myNodes += makeNode(100000000,"Class","circle");
	myNodes += makeNode(101,"Target Image");
	myNodes += makeNode(102,"Target Weight Image");
	myNodes += makeNode(1,"Source Image");
	myNodes += makeNode(2,"Source Weight Image");
	myNodes += makeNode(106,"Catalog");
	myNodes += makeNode(201,"Image");
	myNodes += makeNode(202,"Weight Image");
	myNodes += makeNode(301,"All Images");
	myNodes += makeNode(302,"All Weight Images");
	myNodes += makeNode(303,"All C values");
	myNodes += makeNode(203,"C values");
	myNodes += makeNode(304,"All Mask Images");
	myNodes += makeNode(204,"Mask Image");
	myNodes += makeNode(205,"Segmentation Image");
	myNodes += makeNode(305,"All Segmentation Images");
	myNodes += makeNode(3,"Error Calculation Class","circle");
	myNodes += makeNode(4,"Reprojection Class","circle");
	myNodes += makeNode(5,"Convolution Class","circle");
	myNodes += makeNode(6,"Catalog Creation","circle");
	myNodes += makeNode(7,"Reprojected Image");
	myNodes += makeNode(8,"Reprojected Weight Image");
	myNodes += makeNode(80,"Convoluted Image");
	myNodes += makeNode(500,"Target FWHM","triangle");
	myNodes += makeNode(501,"Source FWHM","triangle");
	myNodes += makeNode(502,"Pixel Scale","triangle");
	myNodes += makeNode(503,"default_objsub_norm.sex","triangle");
	myNodes += makeNode(504, "default_dualimage.sex","triangle");

	
	myConn += makeConn(101,4);
	myConn += makeConn(102,4);
	myConn += makeConn(1,4);
	myConn += makeConn(2,4);
	
	myConn += makeConn(4,8);
	myConn += makeConn(4,7);
	
	myConn += makeConn(101,5);
	myConn += makeConn(7,5);
	myConn += makeConn(500,5);
	myConn += makeConn(501,5);
	myConn += makeConn(5,80);
	myConn += makeConn(201,3);
	myConn += makeConn(202,3);
	myConn += makeConn(502,3);
	myConn += makeConn(503,3);
	myConn += makeConn(3,203);
	myConn += makeConn(3,204);
	myConn += makeConn(3,205);
	myConn += makeConn(6,106);
	myConn += makeConn(301,6);
	myConn += makeConn(302,6);
	myConn += makeConn(303,6);
	myConn += makeConn(304,6);
	myConn += makeConn(305,6);
	myConn += makeConn(504,6);
	
	
	
	//myConn += makeConn(101,201);
	//myConn += makeConn(80,201);
	//myConn += makeConn(102,202);
	//myConn += makeConn(8,202);
	
	//myConn += makeConn(203,303);
	//myConn += makeConn(203,302);
	
	
	
	std::cout<<myNodes;
	std::cout<<myConn;
	
	return 0;
}


/**
int main(){
	std::cout<<"digraph dfa{\n";
	std::string myNodes;
	std::string myConn;
	myNodes += makeNode(100000,"File/Output");
	//myNodes += makeNode(10000,"Needed Elsewhere","invhouse");
	myNodes += makeNode(1000000,"Program","octagon");
	
	if(false){
	myNodes += makeNode(1,"Source Image");
	myNodes += makeNode(2,"Source Weight Image");
	}
	if(false){
	myNodes += makeNode(101,"Image");
	myNodes += makeNode(102,"Weight Image");
	}
	if(false){
	myNodes += makeNode(6,"Segmentation Image");
	myNodes += makeNode(90,"Mask Image");
	myNodes += makeNode(12,"Many Individual Outputs");
	myNodes += makeNode(13,"txt file with locations of these outputs");
	}
	std::cout<<myNodes;
	mainG();
	//mainM();
	//mainC();
	//mainR();
	//mainE();
	//std::cout<<myConn;
	std::cout<<"}\n";
	
	
}
**/

int main(){
	std::cout<<"digraph dfa{\n";
	std::string myNodes;
	std::string myConn;
	//create Nodes by giving them an ID, something to display, and a shape(defaults to rectangle)
	myNodes += makeNode(0,"Ranking the first 7 letters","octagon");
	myNodes += makeNode(100,"Number 1 Vowel");
	myNodes += makeNode(1000,"Number 1 Constant"); //ID's can be arbitrary
	myNodes += makeNode(1,"a","circle");
	myNodes += makeNode(2,"b","circle");
	myNodes += makeNode(3,"c","circle");
	myNodes += makeNode(4,"d","circle");
	myNodes += makeNode(5,"e","circle");
	myNodes += makeNode(6,"f","circle");
	myNodes += makeNode(7,"g","circle");

	myConn += makeConn(100,5); //Draw arrow by linking IDs together
	myConn += makeConn(5,1);
	
	myConn += makeConn(1000,4);
	myConn += makeConn(4,7);
	myConn += makeConn(7,2);
	myConn += makeConn(7,3);
	myConn += makeConn(2,6);
	myConn += makeConn(3,6);

	std::cout<<myNodes;
	std::cout<<myConn;
	std::cout<<"}\n";


}


int main4(){
	int global = 1;
	std::cout<<"digraph dfa{\n";
	std::string myNodes;
	std::string myConn;
	myNodes += makeNode(1000000,"Program","octagon");
	myNodes += makeNode(100000,"File/Output");
	myNodes += makeNode(10000,"Command Line","invhouse");
	myNodes += makeNode(1000,"User Input","triangle");
	myNodes += makeNode(100,"maskitextra.py blue","octagon");
	myNodes += makeNode(1,"maskitextra.py red","octagon");
	myNodes += makeNode(2,"science file red");
	myNodes += makeNode(200,"science file blue");
	myNodes += makeNode(3,"weight file red");
	myNodes += makeNode(300,"weight file blue");
	myNodes += makeNode(4,"mask file red");
	myNodes += makeNode(400,"mask file blue");
	myNodes += makeNode(5,"science newnorm3 red");
	myNodes += makeNode(500,"science newnorm3 blue");
	myNodes += makeNode(6,"reproj_kmj.py","octagon");
	myNodes += makeNode(7,"science reprj blue");
	myNodes += makeNode(8,"weight reprj_wht blue");
	myNodes += makeNode(9,"Convolutin_py3_v2.ipynb","octagon");
	myNodes += makeNode(10,"FWHM red","triangle");
	myNodes += makeNode(1000,"FWHM blue","triangle");
	myNodes += makeNode(11,"Making a Catalog.ipynb","octagon");
	myNodes += makeNode(12,"default_dualimage.sex","triangle");
	myNodes += makeNode(13,"science reprj_conv_bX blue");
	myNodes += makeNode(14,"segmentation seg_newnorm3 red");
	myNodes += makeNode(1400,"segmentation seg_newnorm3 blue");
	myNodes += makeNode(15,"catalog");
	myNodes += makeNode(16,"Sextractor Command Line for Red","invhouse");
	myNodes += makeNode(1600,"Sextractor Command Line for Blue","invhouse");
	myNodes += makeNode(17,"quickmask.py red","octagon");
	myNodes += makeNode(1700,"quickmask.py blue","octagon");
	myNodes += makeNode(18,"object subtracted objsub_newnorm3 red");
	myNodes += makeNode(1800,"object subtracted objsub_newnorm3 blue");
	myNodes += makeNode(19,"runEAA.py red","octagon");
	myNodes += makeNode(1900,"runEAA.py blue","octagon");
	myNodes += makeNode(20,"many outputs red");
	myNodes += makeNode(2000,"many outputs blue");
	myNodes += makeNode(21,"command line for red","invhouse");
	myNodes += makeNode(2100,"command line for blue","invhouse");
	myNodes += makeNode(22,"txt of locations to red outputs");
	myNodes += makeNode(2200,"txt of locations to blue outputs");
	myNodes += makeNode(23,"object subtracted mask objsub_newnorm3_maskd red");
	myNodes += makeNode(2300,"object subtracted mask objsub_newnorm3_maskd blue");
	myNodes += makeNode(24,"WorkingDepth.ipynb","octagon");
	myNodes += makeNode(25,"Pixel Scale","triangle");
	myNodes += makeNode(26,"C values red");
	myNodes += makeNode(2600,"C values blue");
	myConn  += makeConn(2,1);
	myConn  += makeConn(3,1);
	myConn  += makeConn(1,4);
	myConn  += makeConn(1,5);
	myConn  += makeConn(100,400);
	myConn  += makeConn(100,500);
	myConn  += makeConn(2,6);
	myConn  += makeConn(200,6);
	myConn  += makeConn(3,6);
	myConn  += makeConn(300,6);
	myConn  += makeConn(6,7);
	myConn  += makeConn(6,8);
	myConn  += makeConn(1000,9);
	myConn  += makeConn(10,9);
	myConn  += makeConn(2,9);
	myConn  += makeConn(7,9);
	myConn  += makeConn(12,11);
	//myConn  += makeConn(10,12);
	myConn  += makeConn(2,11);
	myConn  += makeConn(13,11);
	myConn  += makeConn(3,11);
	myConn  += makeConn(8,11);
	myConn  += makeConn(400,11);
	myConn  += makeConn(4,11);
	myConn  += makeConn(14,11);
	myConn  += makeConn(1400,11);
	myConn  += makeConn(11,15);
	myConn  += makeConn(11,15);
	myConn  += makeConn(9,13);
	myConn  += makeConn(5,16);
	myConn  += makeConn(500,1600);
	myConn  += makeConn(16,18);
	myConn  += makeConn(16,14);
	myConn  += makeConn(1600,1800);
	myConn  += makeConn(1600,1400);
	myConn  += makeConn(4,17);
	myConn  += makeConn(400,1700);
	myConn  += makeConn(18,17);
	myConn  += makeConn(1800,1700);
	myConn  += makeConn(17,23);
	myConn  += makeConn(1700,2300);
	myConn  += makeConn(19,20);
	myConn  += makeConn(20,21);
	myConn  += makeConn(1900,2000);
	myConn  += makeConn(2000,2100);
	myConn  += makeConn(21,22);
	myConn  += makeConn(2100,2200);
	myConn  += makeConn(23,19);
	myConn  += makeConn(2300,1900);
	myConn  += makeConn(22,24);
	myConn  += makeConn(2200,24);
	myConn  += makeConn(2,24);
	myConn  += makeConn(13,24);
	myConn  += makeConn(25,24);
	myConn  += makeConn(26,11);
	myConn  += makeConn(2600,11);
		myConn  += makeConn(24,2600);
	myConn  += makeConn(24,26);
	myConn  += makeConn(8,100);
	myConn  += makeConn(13,100);
	std::cout<<myNodes;
	std::cout<<myConn;
	std::cout<<"}\n";
	//node1 -> node2 [label=\"arm1\"]
	
	return 0;
}


int main2(){
	int global = 1;
	std::cout<<"digraph dfa{\n";
	std::string myNodes;
	std::string myConn;
	myNodes += makeNode(1,"maskitextra.py");
	myNodes += makeNode(100,"maskitextra.py");
	myNodes += makeNode(2,"science file");
	myNodes += makeNode(3,"weight file");
	myNodes += makeNode(4,"mask file");
	myNodes += makeNode(5,"science newnorm3");
	myNodes += makeNode(6,"reproj_kmj.py");
	myNodes += makeNode(7,"science reprj");
	myNodes += makeNode(8,"weight reprj_wht");
	myNodes += makeNode(9,"Convolutin_py3_v2.ipynb");
	myNodes += makeNode(10,"FWHM");
	myNodes += makeNode(11,"Making a Catalog.ipynb");
	myNodes += makeNode(12,"default_dualimage.sex");
	myNodes += makeNode(13,"science reprj_conv_bX");
	myNodes += makeNode(14,"segmentation seg_newnorm3");
	myNodes += makeNode(15,"catalog");
	myNodes += makeNode(16,"Sextractor Command Line");
	myNodes += makeNode(17,"quickmask.py");
	myNodes += makeNode(18,"object subtracted objsub_newnorm3");
	myNodes += makeNode(19,"runEAA.py");
	myNodes += makeNode(20,"many outputs");
	myNodes += makeNode(21,"command line");
	myNodes += makeNode(22,"txt of locations to outputs");
	myNodes += makeNode(23,"object subtracted mask objsub_newnorm3_maskd");
	myNodes += makeNode(24,"WorkingDepth.ipynb");
	myNodes += makeNode(25,"Pixel Scale");
	myNodes += makeNode(26,"C values");
	myConn  += makeConn(2,1);
	myConn  += makeConn(3,1);
	myConn  += makeConn(1,4);
	myConn  += makeConn(1,5);
	myConn  += makeConn(100,4);
	myConn  += makeConn(100,5);
	myConn  += makeConn(2,6);
	myConn  += makeConn(2,6);
	myConn  += makeConn(6,7);
	myConn  += makeConn(6,8);
	myConn  += makeConn(10,9);
	myConn  += makeConn(10,9);
	myConn  += makeConn(2,9);
	myConn  += makeConn(2,9);
	myConn  += makeConn(7,9);
	myConn  += makeConn(12,11);
	myConn  += makeConn(10,12);
	myConn  += makeConn(2,11);
	myConn  += makeConn(13,11);
	myConn  += makeConn(3,11);
	myConn  += makeConn(8,11);
	myConn  += makeConn(4,11);
	myConn  += makeConn(4,11);
	myConn  += makeConn(14,11);
	myConn  += makeConn(14,11);
	myConn  += makeConn(11,15);
	myConn  += makeConn(11,15);
	myConn  += makeConn(9,13);
	myConn  += makeConn(5,16);
	myConn  += makeConn(16,18);
	myConn  += makeConn(16,14);
	myConn  += makeConn(4,17);
	myConn  += makeConn(18,17);
	myConn  += makeConn(17,23);
	myConn  += makeConn(19,20);
	myConn  += makeConn(20,21);
	myConn  += makeConn(21,22);
	myConn  += makeConn(23,19);
	myConn  += makeConn(22,24);
	myConn  += makeConn(22,24);
	myConn  += makeConn(2,24);
	myConn  += makeConn(13,24);
	myConn  += makeConn(25,24);
	myConn  += makeConn(26,11);
	myConn  += makeConn(26,11);
	myConn  += makeConn(24,26);
	myConn  += makeConn(8,100);
	myConn  += makeConn(13,100);
	std::cout<<myNodes;
	std::cout<<myConn;
	std::cout<<"}\n";
	//node1 -> node2 [label=\"arm1\"]
	
	return 0;
}

int main3(){
		int global = 1;
	std::cout<<"digraph dfa{\n";
	std::string myNodes;
	std::string myConn;
	//myNodes += makeNode(1,"maskitextra.py");
	//myNodes += makeNode(100,"maskitextra.py");
	myNodes += makeNode(2,"science file");
	myNodes += makeNode(3,"weight file");
	myNodes += makeNode(4,"mask file");
	//myNodes += makeNode(5,"science newnorm3");
	myNodes += makeNode(6,"reproj_kmj.py");
	myNodes += makeNode(7,"science reprj");
	myNodes += makeNode(8,"weight reprj_wht");
	myNodes += makeNode(9,"Convolutin_py3_v2.ipynb");
	myNodes += makeNode(10,"FWHM");
	myNodes += makeNode(11,"Making a Catalog.ipynb");
	myNodes += makeNode(12,"default_dualimage.sex");
	myNodes += makeNode(13,"science reprj_conv_bX");
	myNodes += makeNode(14,"segmentation seg_newnorm3");
	myNodes += makeNode(15,"catalog");
	//myNodes += makeNode(16,"Sextractor Command Line");
	//myNodes += makeNode(17,"quickmask.py");
	//myNodes += makeNode(18,"object subtracted objsub_newnorm3");
	//myNodes += makeNode(19,"runEAA.py");
	//myNodes += makeNode(20,"many outputs");
	//myNodes += makeNode(21,"command line");
	//myNodes += makeNode(22,"txt of locations to outputs");
	//myNodes += makeNode(23,"object subtracted mask objsub_newnorm3_maskd");
	//myNodes += makeNode(24,"WorkingDepth.ipynb");
	myNodes += makeNode(25,"Pixel Scale");
	myNodes += makeNode(26,"C values");
	myNodes += makeNode(27,"Empty Apperature Analysis");
	
	myConn  += makeConn(3,6);
	
	myConn  += makeConn(2,27);
	myConn  += makeConn(3,27);
	myConn  += makeConn(13,27);
	myConn  += makeConn(8,27);
	myConn  += makeConn(25,27);
	myConn  += makeConn(27,26);
	myConn  += makeConn(27,26);
	myConn  += makeConn(27,14);
	myConn  += makeConn(27,14);
	myConn  += makeConn(27,4);
	myConn  += makeConn(27,4);
	//myConn  += makeConn(2,1);
	//myConn  += makeConn(3,1);
	//myConn  += makeConn(1,4);
	//myConn  += makeConn(1,5);
	//myConn  += makeConn(100,4);
	//myConn  += makeConn(100,5);
	myConn  += makeConn(2,6);
	myConn  += makeConn(2,6);
	myConn  += makeConn(6,7);
	myConn  += makeConn(6,8);
	myConn  += makeConn(10,9);
	myConn  += makeConn(10,9);
	myConn  += makeConn(2,9);
	myConn  += makeConn(7,9);
	myConn  += makeConn(12,11);
	myConn  += makeConn(10,12);
	myConn  += makeConn(2,11);
	myConn  += makeConn(13,11);
	myConn  += makeConn(3,11);
	myConn  += makeConn(8,11);
	myConn  += makeConn(4,11);
	myConn  += makeConn(4,11);
	myConn  += makeConn(14,11);
	myConn  += makeConn(14,11);
	myConn  += makeConn(11,15);
	myConn  += makeConn(11,15);
	myConn  += makeConn(9,13);
	//myConn  += makeConn(5,16);
	//myConn  += makeConn(16,18);
	//myConn  += makeConn(16,14);
	//myConn  += makeConn(4,17);
	//myConn  += makeConn(18,17);
	//myConn  += makeConn(17,23);
	//myConn  += makeConn(19,20);
	//myConn  += makeConn(20,21);
	//myConn  += makeConn(21,22);
	//myConn  += makeConn(23,19);
	//myConn  += makeConn(22,24);
	//myConn  += makeConn(22,24);
	//myConn  += makeConn(2,24);
	//myConn  += makeConn(13,24);
	//myConn  += makeConn(25,24);
	myConn  += makeConn(26,11);
	myConn  += makeConn(26,11);
	//myConn  += makeConn(24,26);
	//myConn  += makeConn(8,100);
	//myConn  += makeConn(13,100);
	std::cout<<myNodes;
	std::cout<<myConn;
	std::cout<<"}\n";
	//node1 -> node2 [label=\"arm1\"]
	
	return 0;
}
