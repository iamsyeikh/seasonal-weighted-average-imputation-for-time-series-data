Adaptive Weighted Seasonal Imputation merupakan metode imputasi missing value pada data time series yang memanfaatkan dua informasi utama, yaitu:

Pola seasonal (seasonal component) adalah memanfaatkan nilai pada periode seasonal yang sama.
Pola lokal (local component) adalah memanfaatkan nilai yang berada tepat sebelum dan sesudah missing value.

Kedua komponen tersebut kemudian digabungkan menggunakan bobot tertentu untuk menghasilkan nilai estimasi yang digunakan dalam menggantikan missing value.

Metode ini dirancang agar dapat mempertimbangkan pola berulang dalam time series sekaligus kondisi lokal di sekitar missing value.

Ide utama dari metode imputasi ini adalah mengestimasi missing value pada data time series dengan menggabungkan informasi dari **pola seasonal** dan **kondisi lokal** di sekitar data yang hilang. Komponen seasonal diperoleh dari nilai pada periode yang sama, yaitu \(t-2P\), \(t-P\), \(t+P\), dan \(t+2P\), sedangkan komponen lokal diperoleh dari nilai sebelum dan sesudah missing value, yaitu \(t-1\) dan \(t+1\). Kedua komponen tersebut kemudian digabungkan menggunakan bobot tertentu, sehingga hasil imputasi tidak hanya mengikuti pola berulang dalam data, tetapi juga mempertimbangkan perubahan nilai di sekitar titik missing. Apabila salah satu komponen tidak tersedia, metode menggunakan komponen yang tersedia, sedangkan jika keduanya tidak tersedia maka digunakan rata-rata keseluruhan data sebagai nilai pengganti.
