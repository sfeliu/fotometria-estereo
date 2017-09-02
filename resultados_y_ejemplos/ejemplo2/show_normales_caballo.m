function show_normales_caballo()
x=dlmread('normalesPeoresX.txt'); N=x;
y=dlmread('normalesPeoresY.txt'); N(:,:,2)=y;
z=dlmread('normalesPeoresZ.txt'); N(:,:,3)=z;

[height,width,~] = size(N);

[X,Y] = meshgrid(1:width,1:height);
 

%%
Z = zeros(size(N,1),size(N,2));
quiver3(X, Y, Z, N(:,:,1),N(:,:,2),N(:,:,3))


end