%%  修改IEEE-Journal的简写
% author:HenryLiu
%  datetime:2019/9/14 下午 08:43
%  Function:IEEE-transform
%%输入文献为'Ref.bib'，输出文献为'new.bib'
filecontent = importdata('Ref.bib');

refcontent = readtable("A.csv")
abbrcontent = readtable("B.csv")

for i = 1:size(filecontent, 1)
    test = regexpi(filecontent{i}, 'journal');
    if(test)
        [startIndex, endIndex] = regexpi(filecontent{i},'{(.*?)}');
        journal = filecontent{i};
        if(journal(startIndex+1:endIndex-1))
            word_previous = journal(startIndex+1:endIndex-1);
        else
            [startIndex, endIndex] = regexpi(filecontent{i},'"(.*?)"');
            journal = filecontent{i}; 
            word_previous = journal(startIndex+1:endIndex-1);
        end
        word_previous = strtrim(word_previous);
        
        for j = 1:size(refcontent, 1)
            word = refcontent{j,1};
            word = word{1,1};
            if(strcmpi(word, word_previous))
                word_transform = refcontent{j, 2};
                word_transform = word_transform{1, 1};
                filecontent{i} = strrep(filecontent{i}, word_previous, word_transform);
            end
        end       
        
        word_list = regexp(word_previous, ' ', 'split');
        for k = 1:size(word_list, 2)
            for j = 1:size(abbrcontent, 1)
                word = abbrcontent{j,1};
                word = word{1,1};
                if(strcmpi(word, word_list{k}))
                    word_transform = abbrcontent{j, 2};
                    word_transform = word_transform{1, 1};
                    filecontent{i} = strrep(filecontent{i}, word_list{k}, word_transform);
                end
            end
        end        
        
 
    end
end
writecell(filecontent, 'new.txt',"QuoteStrings",false)
eval(['!rename',',new.txt,' ',new.bib'])