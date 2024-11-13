package domain;

public class Entity<ID> {
    private ID id;
    public void setId(ID newId){
        id = newId;
    }
    public ID getId(){
        return id;
    }
}
