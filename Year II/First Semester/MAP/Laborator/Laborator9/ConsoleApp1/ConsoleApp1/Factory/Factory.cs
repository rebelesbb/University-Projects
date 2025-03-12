using ConsoleApp1.Model;

namespace ConsoleApp1.Factory;

public interface Factory
{
    Container createContainer(Strategy strategy);
}