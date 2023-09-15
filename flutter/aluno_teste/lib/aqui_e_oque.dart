import 'dart:convert';
import 'dart:ffi';
import 'dart:io';
import 'package:testes/models/utils.dart';
import 'package:testes/models/alunos.dart';

void execute() {
  var aluno1 = Aluno('Débora Monic');

  print("Bem vindo ao sistema de notas");
  String nomeAluno =
      Consoleutils.lerStringComTexto("Informe o nome do aluno: ");
  var aluno2 = Aluno(nomeAluno);
  double? nota1;
  do {
    nota1 =
        Consoleutils.lerDoubleComTexto("Insira a sua nota ou 'Q' para sair");
    if (nota1 != null) {
      aluno1.addNota(nota1);
    }
  } while (nota1 != null);
  print(aluno1.getNotas());
}
