Rumus matematis dari fungsi Adaptive Weighted Seasonal Imputation Anda dapat dituliskan sebagai berikut.

Misalkan:

\(x_t\) = nilai time series pada waktu \(t\)
\(P\) = seasonal_period
\(w_c\) = current_weight
\(w_p\) = bobot masing-masing nilai sebelum center
\(C_k\) = posisi center pada siklus seasonal ke-\(k\)
1. Bobot

Kode Anda menetapkan:

$$ w_c = \text{current\_weight} $$

dan:

$$ w_p = \frac{1-w_c}{P-1} $$

Dengan default:

$$ w_c=0.50 $$

maka:

$$ w_p=\frac{0.50}{P-1} $$

Contoh \(P=7\):

$$ w_p=\frac{0.50}{6}=0.08333 $$

Jadi bobotnya:

$$ \boxed{0.50 + 6(0.08333)=1} $$
2. Membentuk seasonal window

Untuk missing value pada posisi \(t\), algoritma mencari center:

$$ C_1=t-P $$

kemudian:

$$ C_2=t-2P $$ $$ C_3=t-3P $$

dan seterusnya sampai tidak ada lagi data historis.

Pada setiap \(C_k\), algoritma mengambil:

$$ x_{C_k} $$

serta \(P-1\) nilai sebelumnya:

$$ x_{C_k-1},x_{C_k-2},\ldots,x_{C_k-(P-1)} $$
3. Weighted Mean

Prediksi pada setiap seasonal cycle adalah:

$$ \hat{x}_{t,k} = \frac{ w_c x_{C_k} + w_p\displaystyle\sum_{i=1}^{P-1}x_{C_k-i} }{ w_c+w_p(P-1) } $$

Namun kode Anda memiliki normalisasi bobot ketika terdapat NaN.

Jadi bentuk yang lebih tepat adalah:

$$ \boxed{ \hat{x}_{t,k} = \frac{ \displaystyle\sum_{j\in V_k}w_jx_j }{ \displaystyle\sum_{j\in V_k}w_j } } $$

dengan:

\(V_k\) = kumpulan nilai yang tersedia/tidak NaN
\(w_j=w_c\) untuk nilai center
\(w_j=w_p\) untuk nilai sebelumnya.
4. Jika semua nilai tersedia

Misalnya:

$$ P=7 $$

dan:

$$ w_c=0.5 $$

maka:

$$ w_p=\frac{0.5}{6}=0.08333 $$

Jika:

$$ C_k=t-7 $$

maka:

$$ \hat{x}_{t,k} = 0.5x_{t-7} + 0.08333x_{t-8} + 0.08333x_{t-9} + 0.08333x_{t-10} + 0.08333x_{t-11} + 0.08333x_{t-12} + 0.08333x_{t-13} $$

Karena jumlah bobotnya 1.

5. Menggunakan beberapa seasonal cycle

Misalnya tersedia tiga prediksi:

$$ \hat{x}_{t,1},\hat{x}_{t,2},\hat{x}_{t,3} $$

Maka hasil akhir kode Anda adalah rata-rata dari semua seasonal prediction:

$$ \boxed{ \hat{x}_t= \frac{1}{K} \sum_{k=1}^{K}\hat{x}_{t,k} } $$

dengan \(K\) = jumlah seasonal cycle yang berhasil digunakan.

6. Secara keseluruhan

Rumus metode Anda dapat diringkas menjadi:

$$ \boxed{ \hat{x}_t= \frac{1}{K} \sum_{k=1}^{K} \left( \frac{ \displaystyle\sum_{j\in V_k}w_jx_j }{ \displaystyle\sum_{j\in V_k}w_j } \right) } $$

dengan:

$$ w_c=\alpha $$ $$ w_p=\frac{1-\alpha}{P-1} $$

sehingga:

$$ \boxed{ \hat{x}_t= \frac{1}{K} \sum_{k=1}^{K} \frac{ \alpha x_{C_k} + \frac{1-\alpha}{P-1} \displaystyle\sum_{i=1}^{P-1}x_{C_k-i} }{ \alpha+ \frac{1-\alpha}{P-1}(P-1) } } $$

untuk kondisi ketika seluruh nilai tersedia.

Dengan \alpha=0.5, metode Anda pada dasarnya memberikan 50% bobot kepada nilai pada posisi seasonal yang sama dan 50% sisanya dibagi rata kepada \(P-1\) nilai sebelumnya, kemudian hasil dari beberapa siklus seasonal dirata-ratakan.

Catatan penting untuk penulisan skripsi: istilah adaptive pada implementasi ini terutama berasal dari normalisasi bobot ketika sebagian nilai dalam window mengalami missing value. Bobot dasarnya sendiri (current_weight) tetap, bukan dipelajari atau dioptimalkan secara otomatis.
