"""Baseline

Revision ID: 35a0f50b9635
Revises: 
Create Date: 2023-04-09 15:38:51.944376

"""
import uuid
from alembic import op
from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    Float,
    Integer,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
    func,
)


# revision identifiers, used by Alembic.
revision = "35a0f50b9635"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "product",
        Column("product_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("product_name", String(256), nullable=False),
        Column("unit_price", Float, nullable=False),
        Column("product_country", String()),
        Column("time_created", DateTime(timezone=True), server_default=func.now()),
        Column("time_updated", DateTime(timezone=True), onupdate=func.now()),
        PrimaryKeyConstraint("product_id"),
    )

    op.create_table(
        "provider",
        Column("provider_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("quantity", Integer(), nullable=False),
        Column("provide_date", DateTime(), server_default=func.now()),
        Column("time_created", DateTime(timezone=True), server_default=func.now()),
        Column("time_updated", DateTime(timezone=True), onupdate=func.now()),
        PrimaryKeyConstraint("provider_id"),
    )

    op.create_table(
        "product_provider_association",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("product_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("provider_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        UniqueConstraint(
            "product_id", "provider_id", name="uix_product_provider_association"
        ),
    )

    op.create_index(
        op.f("ix_product_provider_association_product_id"),
        "product_provider_association",
        ["product_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_product_provider_association_provider_id"),
        "product_provider_association",
        ["provider_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        op.f("ix_product_provider_association_product_id"),
        table_name="product_provider_association",
    )
    op.drop_index(
        op.f("ix_product_provider_association_provider_id"),
        table_name="product_provider_association",
    )
    op.drop_table("product_provider_association")
    op.drop_table("product")
    op.drop_table("provider")
