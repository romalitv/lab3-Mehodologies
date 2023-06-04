FROM golang:latest AS builder

WORKDIR /app

COPY go.mod ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o build/fizzbuzz

FROM scratch

COPY --from=builder /app/build/fizzbuzz /

COPY --from=builder /app/templates/index.html /templates/

CMD ["/fizzbuzz", "serve"]