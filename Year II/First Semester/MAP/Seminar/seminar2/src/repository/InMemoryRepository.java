package repository;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class InMemoryRepository<ID, E extends Entity<ID>> implements Repository<ID, E> {
    private final Map<ID, E> map;

    public InMemoryRepository() {
        map = new ConcurrentHashMap<>();
    }

    @Override
    public E findOne(ID id) {
        if(id == null)
            throw new IllegalArgumentException("id is null");
        return map.get(id);
    }

    @Override
    public Iterable<E> findAll() {
        return map.values();
    }

    @Override
    public E save(E entity) {
        if(entity == null) {
            throw new IllegalArgumentException("Entity cannot be null");
        }
        if(map.containsKey(entity.getId())) {
            return entity;
        }
        else {
            map.put(entity.getId(), entity);
            return null;
        }
    }
}
