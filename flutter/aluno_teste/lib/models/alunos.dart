class Aluno {
  String _nome = "";
  final List<double> _notas = []; //não entnedi o que é esse final

  Aluno(String nome) {
    _nome = nome;
  }
  void setNome(String nome) {
    _nome = nome;
  }

  String getNome() {
    return _nome;
  }

  List<double> getNotas() {
    return _notas;
  }

  void addNota(double nota) {
    _notas.add(nota);
  }
}
