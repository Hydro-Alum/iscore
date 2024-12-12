"""empty message

Revision ID: 3cde10e0aa3a
Revises: 
Create Date: 2024-11-29 17:32:36.128815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cde10e0aa3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('managements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('image', sa.String(length=20), nullable=False),
    sa.Column('role', sa.String(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('school_sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session', sa.String(length=20), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sID', sa.String(length=20), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('middle_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.Column('sex', sa.String(length=6), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('department', sa.String(length=60), nullable=False),
    sa.Column('student_class', sa.String(length=60), nullable=False),
    sa.Column('parent_number', sa.String(length=20), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('picture', sa.String(length=20), nullable=False),
    sa.Column('role', sa.String(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('sID')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('class_range', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tID', sa.String(length=20), nullable=True),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('middle_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('section', sa.String(length=120), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('sex', sa.String(length=6), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('picture', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('role', sa.String(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tID')
    )
    op.create_table('terms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(length=20), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=120), nullable=False),
    sa.Column('test_score', sa.String(), nullable=True),
    sa.Column('practical_score', sa.String(), nullable=True),
    sa.Column('exam_score', sa.String(), nullable=True),
    sa.Column('total_score', sa.String(), nullable=True),
    sa.Column('term', sa.String(length=120), nullable=False),
    sa.Column('session', sa.String(length=120), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('terms')
    op.drop_table('teachers')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('school_sessions')
    op.drop_table('managements')
    # ### end Alembic commands ###