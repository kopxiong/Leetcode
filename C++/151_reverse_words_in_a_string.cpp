// Given an input string, reverse the string word by word.

// 1) Reverse the individual words, we get the below string.
//      "i ekil siht margorp yrev hcum"
// 2) Reverse the whole string from start to end and you get the desired output.
//      "much very program this like i"

#include <iostream>

// function prototype for utility function to reverse a string from begin to end
void reverse(char *begin, char *end);

void reverseWords(char *s)
{
	char *word_begin = NULL;
	char *temp = s;    // temp is for word boundry

	// STEP 1 of the above algorithm
	while (*temp)
	{
		// To make sure that the string start with valid character (not space) only
		if ((word_begin == NULL) && (*temp != ' '))
		{
			word_begin = temp;
		}
		if (word_begin && ((*(temp+1) == ' ') || (*(temp+1) == '\0')))
		{
			reverse(word_begin, temp);
			word_begin = NULL;
		}
		temp++;
	}

	// STEP 2 of the above algorithm
	reverse(s, temp-1);
}

// UTILITY FUNCTIONS
// Function to reverse any sequence starting with pointer begin and ending with pointer end
void reverse(char *begin, char *end)
{
    char temp;
    while (begin < end)
    {
    	temp = *begin;
    	*begin++ = *end;
    	*end-- = temp;
    }
}


int main()
{
    char s[] = "we like this program very much";
    // std::string s("we like this program very much");
    reverseWords(s);
    std::cout << "The reversed string is: " << s << std::endl;

    return 0;
}
