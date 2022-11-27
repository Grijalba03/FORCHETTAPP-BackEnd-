"""empty message

Revision ID: a84c18886ca9
Revises: 
Create Date: 2022-11-23 21:40:29.476211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a84c18886ca9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocked',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blocked_token', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('nutritional_facts', sa.String(length=250), nullable=False),
    sa.Column('information', sa.String(length=250), nullable=True),
    sa.Column('preparation', sa.String(length=250), nullable=True),
    sa.Column('ingredients', sa.String(length=500), nullable=True),
    sa.Column('free_of', sa.String(length=500), nullable=False),
    sa.Column('recipeImage', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recommendations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('recipe_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('dietaryPreferences', sa.String(length=100), nullable=True),
    sa.Column('userTitle', sa.String(length=100), nullable=True),
    sa.Column('userstatus', sa.Boolean(), nullable=True),
    sa.Column('userFacebook', sa.String(length=100), nullable=True),
    sa.Column('userTwitter', sa.String(length=100), nullable=True),
    sa.Column('userInstagram', sa.String(length=100), nullable=True),
    sa.Column('userYoutube', sa.String(length=100), nullable=True),
    sa.Column('userImage', sa.String(length=100), nullable=True),
    sa.Column('userRecipe', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=250), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite__recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    op.drop_table('favorite__recipes')
    op.drop_table('categories')
    op.drop_table('user')
    op.drop_table('reviews')
    op.drop_table('recommendations')
    op.drop_table('recipe')
    op.drop_table('blocked')
    # ### end Alembic commands ###