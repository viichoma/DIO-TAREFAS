import java.util.List;

public class Banco {

    private String nome;
    private List<Conta> contas;

    Banco(String NomeBanco){
        this.nome = NomeBanco;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void getContas() {
        for(Conta c : contas){
            System.out.println(c.toString());
        }
    }

    public void setContas(List<Conta> contas) {
        this.contas = contas;
    }

}