function show_model()

%%
%fnameZ = 'buda.depths.dat';
fnameN = 'buda.normals.dat';

N = read_normals(fnameN);
%Z = read_depths(fnameZ);

[height,width] = size(N);

[X,Y] = meshgrid(1:width,1:height);

figure,surf(X,Y,N);
figure,mesh(X,Y,N);


end
