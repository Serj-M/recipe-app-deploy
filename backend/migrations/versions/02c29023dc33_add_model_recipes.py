"""
Add model recipes

Revision ID: 02c29023dc33
Revises: 
Create Date: 2023-05-16 12:24:27.397951
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02c29023dc33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'recipes',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.Text(), nullable=False),
        sa.Column('ingredients', sa.Text(), nullable=False),
        sa.Column('instructions', sa.Text(), nullable=False),
        sa.Column('time', sa.Integer(), nullable=False),
        sa.CheckConstraint('time > 0', name='time_check'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_recipes_id'), 'recipes', ['id'], unique=False)

    op.create_table(
        'tags',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('tag', sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('tag')
    )

    op.create_table(
        'recipes_tags',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('recipe_id', sa.Integer(), nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
        sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('recipe_id', 'tag_id')
    )

    op.execute(
        """
        INSERT INTO tags (id, tag) 
        VALUES
            (1, 'breakfast'),
            (2, 'lunch'),
            (3, 'dinner'),
            (4, 'dessert');
        """
    )
    op.execute(
        """
        COMMIT;
        """
    )

    op.execute(
        """
        INSERT INTO recipes (title, ingredients, instructions, time)
        VALUES
            ('Pancakes', 'Flour, Eggs, Milk, Salt, Sugar, Oil', 'Mix flour, eggs, milk, salt, and sugar in a bowl until smooth. Heat and grease a skillet. Pour the batter onto the skillet and cook until golden brown on both sides.  Repeat with the remaining batter. Serve the pancakes with your favorite fillings or toppings.', 1);
        """
    )
    op.execute(
        """
        COMMIT;
        """
    )

    op.execute(
        """
        INSERT INTO recipes_tags (recipe_id, tag_id)
        VALUES
            (1, 1),
            (1, 2);
        """
    )
    op.execute(
        """
        COMMIT;
        """
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes_tags')
    op.drop_table('tags')
    op.drop_index(op.f('ix_recipes_id'), table_name='recipes')
    op.drop_table('recipes')
    # ### end Alembic commands ###
