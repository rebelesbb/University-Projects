package com.example.scheletseminar9.util.paging;

public class Pageable {
    private int pageNumber;
    private int pageSize;

    public Pageable(int pageNumber, int pageSize) {
        this.pageNumber = pageNumber;
        this.pageSize = pageSize;
    }

    public int getPageNumber() {
        return pageNumber;
    }

    public int getPageSize() {
        return pageSize;
    }
}
