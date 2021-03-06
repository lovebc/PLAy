"""empty message

Revision ID: 36650ce231bc
Revises: 7321bd8bfdc
Create Date: 2015-07-22 15:16:24.881000

"""

# revision identifiers, used by Alembic.
revision = '36650ce231bc'
down_revision = '7321bd8bfdc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('mturkcompletioncode', sa.String(length=255), nullable=True))
    op.add_column('userinfo_expert', sa.Column('game_primary_other', sa.Text(), nullable=True))
    op.add_column('userinfo_expert', sa.Column('game_primary_other_level', sa.Text(), nullable=True))
    op.add_column('userinfo_expert', sa.Column('game_primary_other_reason', sa.Text(), nullable=True))
    op.add_column('userinfo_expert', sa.Column('specific_counterstrike_weapon', sa.Text(), nullable=True))
    op.add_column('userinfo_expert', sa.Column('specific_dota_hero', sa.Text(), nullable=True))
    op.add_column('userinfo_expert', sa.Column('specific_starcraft_races', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userinfo_expert', 'specific_starcraft_races')
    op.drop_column('userinfo_expert', 'specific_dota_hero')
    op.drop_column('userinfo_expert', 'specific_counterstrike_weapon')
    op.drop_column('userinfo_expert', 'game_primary_other_reason')
    op.drop_column('userinfo_expert', 'game_primary_other_level')
    op.drop_column('userinfo_expert', 'game_primary_other')
    op.drop_column('user', 'mturkcompletioncode')
    ### end Alembic commands ###
