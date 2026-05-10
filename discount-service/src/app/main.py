from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Discount Service")

PROMO_CODES: dict[str, float] = {
    "STUDENT10": 10.0,
    "SALE20": 20.0,
    "VIP30": 30.0,
}

BULK_THRESHOLD = 10
BULK_DISCOUNT = 15.0

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    promo_code: str | None = None

class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}


@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(req: DiscountRequest) -> DiscountResponse:
    if req.promo_code:
        code = req.promo_code.upper()
        if code in PROMO_CODES:
            percent = PROMO_CODES[code]
            return DiscountResponse(
                discount_percent=percent,
                reason=f"Promo code '{code}' applied: {percent}% off",
            )
        else:
            return DiscountResponse(
                discount_percent=0.0,
                reason=f"Promo code '{req.promo_code}' is not valid",
            )

    if req.quantity >= BULK_THRESHOLD:
        return DiscountResponse(
            discount_percent=BULK_DISCOUNT,
            reason=f"Bulk discount: {BULK_DISCOUNT}% off for {req.quantity} items",
        )

    return DiscountResponse(
        discount_percent=0.0,
        reason="No discount applicable",
    )
