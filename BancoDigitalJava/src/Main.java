import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Banco Sicredi = new Banco("Sicredi");
        Cliente venilton = new Cliente();
        venilton.setNome("Venilton");

        Conta cc = new ContaCorrente(venilton);
        Conta poupanca = new ContaPoupanca(venilton);
        List<Conta> ContasSicredi = new ArrayList<Conta>();
        ContasSicredi.add(cc);
        ContasSicredi.add(poupanca);
        Sicredi.setContas(ContasSicredi);
        Sicredi.getContas();

        cc.depositar(100);
        cc.transferir(100, poupanca);

        cc.imprimirExtrato();
        poupanca.imprimirExtrato();
    }

}