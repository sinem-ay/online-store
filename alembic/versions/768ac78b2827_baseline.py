"""baseline

Revision ID: 768ac78b2827
Revises: 
Create Date: 2022-10-12 12:44:57.505371

"""
import uuid

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '768ac78b2827'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import ForeignKey


def upgrade():
    op.create_table(
        'products',
        sa.Column('product_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('product_name', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table(
        'providers',
        sa.Column('provider_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('product_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('total_price', sa.Float(), nullable=False),
        sa.Column('date', sa.DateTime(), server_default=sa.func.now()),

    )
    op.create_foreign_key(
        None, 'providers', 'products', ['product_id'], ['product_id']
    )
    op.create_table(
        'customers',
        sa.Column('customer_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('customer_name', sa.String()),
        sa.Column('customer_email', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table('products')
    op.drop_table('providers')
    op.drop_table('customers')
