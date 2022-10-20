"""change provider id type

Revision ID: 7aa311dca67f
Revises: 768ac78b2827
Create Date: 2022-10-20 15:35:34.534114

"""
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '7aa311dca67f'
down_revision = '768ac78b2827'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('providers', 'provider_id')
    op.add_column('providers',
                  sa.Column('provider_id', sa.Integer, primary_key=True, nullable=False))


def downgrade():
    op.drop_column('providers', 'provider_id')
    op.add_column('providers',
                  sa.Column('provider_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))

