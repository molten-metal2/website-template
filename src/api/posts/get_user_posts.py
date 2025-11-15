from utils.response_builder import success_response, error_handler
from utils.helpers import get_user_id_from_event, get_table, get_query_param

table = get_table('POSTS_TABLE_NAME')

@error_handler
def lambda_handler(event, context):
    """
    GET /posts/user - Get all posts for the authenticated user
    GET /posts/user?user_id={id} - Get all posts for specific user
    Authenticated endpoint - requires valid JWT token
    """
    # Extract authenticated user_id from Cognito authorizer claims (for authorization)
    auth_user_id = get_user_id_from_event(event)
    
    # Check if requesting another user's posts via query parameter
    target_user_id = get_query_param(event, 'user_id', auth_user_id)
    
    # Query posts by user_id using GSI
    response = table.query(
        IndexName='UserIdIndex',
        KeyConditionExpression='user_id = :user_id',
        ExpressionAttributeValues={
            ':user_id': target_user_id
        },
        ScanIndexForward=False  # Sort by created_at descending (newest first)
    )
    
    posts = response.get('Items', [])
    
    return success_response(posts)

