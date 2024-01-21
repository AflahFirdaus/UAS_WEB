from flask import Flask, jsonify, request

app = Flask(__name__)

# Data mahasiswa dalam bentuk list of dictionaries
mahasiswa = [
    {"nim": "3435656", "nama": "Dino", "jurusan": "Informatika"},
    {"nim": "4923722", "nama": "Bobi", "jurusan": "Teknik Elektro"}
]

# Endpoint untuk mendapatkan semua data mahasiswa
@app.route('/mahasiswa', methods=['GET'])
def get_mahasiswa():
    return jsonify(mahasiswa)

# Endpoint untuk mendapatkan data mahasiswa berdasarkan NIM
@app.route('/mahasiswa/<string:nim>', methods=['GET'])
def get_mahasiswa_by_nim(nim):
    for mhs in mahasiswa:
        if mhs['nim'] == nim:
            return jsonify(mhs)
    return jsonify({'message': 'Mahasiswa tidak ditemukan'}), 404

# Endpoint untuk menambahkan data mahasiswa baru
@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    new_mahasiswa = request.get_json()
    mahasiswa.append(new_mahasiswa)
    return jsonify({'message': 'Mahasiswa berhasil ditambahkan'}), 201

# Endpoint untuk mengubah data mahasiswa berdasarkan NIM
@app.route('/mahasiswa/<string:nim>', methods=['PUT'])
def update_mahasiswa(nim):
    for mhs in mahasiswa:
        if mhs['nim'] == nim:
            mhs.update(request.get_json())
            return jsonify({'message': 'Data mahasiswa berhasil diupdate'})
    return jsonify({'message': 'Mahasiswa tidak ditemukan'}), 404

# Endpoint untuk menghapus data mahasiswa berdasarkan NIM
@app.route('/mahasiswa/<string:nim>', methods=['DELETE'])
def delete_mahasiswa(nim):
    for mhs in mahasiswa:
        if mhs['nim'] == nim:
            mahasiswa.remove(mhs)
            return jsonify({'message': 'Data mahasiswa berhasil dihapus'})
    return jsonify({'message': 'Mahasiswa tidak ditemukan'}), 404

if __name__ == '__main__':
    app.run(debug=True)
