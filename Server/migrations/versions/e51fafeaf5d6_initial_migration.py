"""initial migration

Revision ID: e51fafeaf5d6
Revises: 
Create Date: 2023-11-28 12:13:40.156640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e51fafeaf5d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clothes',
    sa.Column('clothes_id', sa.Integer(), nullable=False),
    sa.Column('designer_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('clothes_id', name=op.f('pk_clothes'))
    )
    op.create_table('designer',
    sa.Column('designer_id', sa.Integer(), nullable=False),
    sa.Column('name_of_designer', sa.String(length=100), nullable=False),
    sa.Column('store_location', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('designer_id', name=op.f('pk_designer'))
    )
    op.create_table('cdassociation',
    sa.Column('cd_id', sa.Integer(), nullable=False),
    sa.Column('clothes_id', sa.Integer(), nullable=True),
    sa.Column('designer_id', sa.Integer(), nullable=True),
    sa.Column('item_in_stock', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['clothes_id'], ['clothes.clothes_id'], name=op.f('fk_cdassociation_clothes_id_clothes')),
    sa.ForeignKeyConstraint(['designer_id'], ['designer.designer_id'], name=op.f('fk_cdassociation_designer_id_designer')),
    sa.PrimaryKeyConstraint('cd_id', name=op.f('pk_cdassociation'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cdassociation')
    op.drop_table('designer')
    op.drop_table('clothes')
    # ### end Alembic commands ###
