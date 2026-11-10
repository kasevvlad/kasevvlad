## Hi, I'm Vladislav Kasev

Backend developer from Uzbekistan. I build APIs in PHP with Laravel and Symfony and care most about the parts that break in production: retries, race conditions, data consistency. Lately I'm writing Go as well.

**Stack:** PHP · Laravel · Symfony · API Platform · PostgreSQL · MySQL · Docker · Vue · TypeScript · Go

### Open source

**[idempotency](https://github.com/kasevvlad/idempotency)** — `Idempotency-Key` header support for Laravel and Symfony. A retried `POST` gets the stored response instead of charging the customer twice; concurrent duplicates get `409`, a reused key with a different payload gets `422`.

```bash
composer require kasevvlad/idempotency
```

### What I'm into

- Domain-driven design and clear boundaries inside PHP applications
- Reliable APIs: idempotency, queues, the outbox pattern
- Go for small, fast services

### Contact

vladkasev13@gmail.com
